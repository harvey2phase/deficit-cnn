#-------------------------------------------------------------------------------
# Imports and constants
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import os


DECADE_RANGE = range(8, 9)
YEAR_RANGE = range(10)

MATRIX_WIDTH_RANGE = range(1, 120) # Ignore t=1, since all nodes start at 0
MATRIX_LENGTH_RANGE = range(50)

#-------------------------------------------------------------------------------
# Generic Transform and Writing Functions
#-------------------------------------------------------------------------------

# This function takes in an output 2D matrix, then writes the matrix to the
#   file (creates the file if it does not exist).
# Parameters:
#   output_dir: specifies the directory to create the file in
#   file_name: specifies the filename
#   matrix: specifies the matrix to write
def write_to_file(output_dir, filename, matrix):
    f = open(output_dir + filename, "w")
    for m in matrix:
        f.write(" ".join(map(str, m)) + "\n")
    f.close()

# This function transforms all the data (.txt) in one directory
# Parameters:
#   input_folder: specifies the directory that contains subdirectories of data;
#     the subdirectories have names "X0", where X is the decade
#     (e.g. "matrix_50nodes")
#   output_folder: specifies the directory to output the data in subdirectories;
#     the subdirectories have names "X0", where X is the decade
#   function: specifies the transformation for the data,
#     takes in the input directory and filename and returns the output data
def transform(
    input_folder,
    transform_function,
    transform_param
):
    input_folder += "/"

    # Iterate through all decade folders
    for decade in DECADE_RANGE:
        decade = str(decade)
        input_dir = input_folder + decade + "0/"

        # Iterate through all the years in the decade folder
        for filename in os.listdir(input_dir):
            print(filename)
            output = transform_function(
                input_dir,
                filename,
                transform_param
            )

# This function transforms all the data (.txt) in one directory and writes it in
#   another
# Parameters:
#   input_folder: specifies the directory that contains subdirectories of data;
#     the subdirectories have names "X0", where X is the decade
#     (e.g. "matrix_50nodes")
#   output_folder: specifies the directory to output the data in subdirectories;
#     the subdirectories have names "X0", where X is the decade
#   function: specifies the transformation for the data,
#     takes in the input directory and filename and returns the output data
def transform_and_write(
    input_folder,
    output_folder,
    transform_function,
    transform_param
):
    input_folder += "/"
    output_folder += "/"

    # Iterate through all decade folders
    for decade in DECADE_RANGE:
        decade = str(decade)
        input_dir = input_folder + decade + "0/"
        output_dir = output_folder + decade + "0/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Iterate through all the years in the decade folder
        for filename in os.listdir(input_dir):
            print(filename)
            output = transform_function(
                input_dir,
                filename,
                transform_param
            )
            write_to_file(output_dir, filename, output)

# This function takes in a data folder and plot the data inside it to a plot
#   folder
# Parameter:
#   data_folder: Specfifies the directory for the data
#   plot_folder: Specfifies the directory for the plots
#   plot_function: A function from plt to plot the data
def plot_data(data_folder, plot_folder, plot_function):
    data_folder += "/"
    plot_folder += "/"

    # Iterate through all decade folders
    for decade in DECADE_RANGE:
        decade = str(decade)
        data_dir = data_folder + decade + "0/"
        plot_dir = plot_folder + decade + "0/"
        if not os.path.exists(plot_dir):
            os.makedirs(plot_dir)

        # Iterate through all the years in the decade folder
        for year in YEAR_RANGE:
            year = str(year)
            filename = decade + year

            # Iterate through all duplicates of the year
            duplicate = 2
            while os.path.isfile(data_dir + filename + ".txt"):
                data = np.loadtxt(data_dir + filename + ".txt")
                plot_function(data)
                plt.savefig(plot_dir + filename)

                filename = decade + year + "(" + str(duplicate) + ")"
                duplicate += 1

#-------------------------------------------------------------------------------
# Transformations
#-------------------------------------------------------------------------------

def dot_to_line_matrix(input_folder, filename, param):
    matrix = np.loadtxt(input_folder + filename)

    if (str.isdigit(filename[2])):
        death_age = int(filename[0] + filename[1] + filename[2], 10)
    else:
        death_age = int(filename[0] + filename[1], 10)

    for w in MATRIX_WIDTH_RANGE:

        if w > death_age:
            for l in MATRIX_LENGTH_RANGE:
                matrix[l][w] = -2
            break

        for l in MATRIX_LENGTH_RANGE:
            if (matrix[l][w] == 0):
                matrix[l][w] = matrix[l][w-1]
            elif (matrix[l][w] == -1):
                matrix[l][w] = 0

    return matrix

# This function truncates line images to x-year-period health state y years
#   before death.
# Healthy nodes are represented as zeros; damaged nodes are represented with an
#   integer that corresponds to the decade in which the data is in.
#   (e.g. 4 represents damaged nodes at age 40 and 8 at 80 instead of all 1)
# Parameters:
#   input_folder: folder that contains line matrices
#   filenmae: filename
#   xy: int array that contains x and y at indices 0 and 1, repsectively
def x_year_data_y_year_before_death(input_folder, filename, xy):
    x, y = xy[0], xy[1]
    matrix = np.loadtxt(input_folder + filename)

    if (str.isdigit(filename[2])):
        death_age = int(filename[0] + filename[1] + filename[2], 10)
    else:
        death_age = int(filename[0] + filename[1], 10)

    w = death_age - y - x
    while w < death_age - y:
        for l in MATRIX_LENGTH_RANGE:
            if (matrix[l][w] == 1):
                matrix[l][w] = int (w / 10)

        w += 1

    return matrix[:, death_age - y - x : death_age - y]

# This function truncates line matrices of 80+ year-olds to matrices that
#   include the health states between 80 and 80-x years, and assigns labels
#   based whether the individual is dead y years after age 80.
# The function appends the truncated matrices in a training file and the labels
#   in a label file. Inidividuals are labeled 1 if they die within y years after
#   age 80, and labeled 0 otherwise
# Parameters:
#   input_folder: folder that contains line matrices
#   filenmae: filename
#   params: string array that contains the following
#     matrix_file: the path to the matrix data file to be written
#     label_file: the path to the label file to be written
#     x: the number of years before 80 to record
#     y: if the individual is dead at/before age 80+y, it is given a label 1
def x_years_before_80_dead_in_y_years(input_folder, filename, params):
    matrix_filename = params[0]
    label_filename = params[1]
    x = int(params[2])
    y = int(params[3])

    matrix = np.loadtxt(input_folder + filename)

    death_age = int(filename[0] + filename[1], 10)

    matrix_file = open(matrix_filename, "a+")
    matrix_file.write(matrix[:, 80 - x : 80])
    matrix_file.close()

    label_file = open(label_filename, "a+")
    if (death_age <= 80 + y):
        label_file.write(1)
    else:
        label_file.write(0)
    label_file.close()


#-------------------------------------------------------------------------------
# Scripts
#-------------------------------------------------------------------------------

'''
transform_and_write(
    "matrices/e5/50_annk/dot",
    "matrices/e5/50_annk/line",
    dot_to_line_matrix,
    None
)
'''

transform(
    "../cnn/data_sets/e5/prob_of_death_at_80/train_individuals",
    x_years_before_80_dead_in_y_years,
    ["../cnn/data_sets/e5/prob_of_death_at_80/train_set.txt",
        "../cnn/data_sets/e5/prob_of_death_at_80/train_labels.txt", "5", "5"]
)

'''
transform_and_write(
    "e4_training_individuals",
    "e4_training_individuals/7_death_5_years",
    x_year_data_y_year_before_death,
    [7, 5]
)
transform_and_write(
    "e4_training_individuals",
    "e4_training_individuals/7_death_12_years",
    x_year_data_y_year_before_death,
    [7, 12]
)
transform_and_write(
    "e4_eval_individuals",
    "e4_eval_individuals/7_death_5_years",
    x_year_data_y_year_before_death,
    [7, 5]
)
transform_and_write(
    "e4_eval_individuals",
    "e4_eval_individuals/7_death_12_years",
    x_year_data_y_year_before_death,
    [7, 12]
)
'''
