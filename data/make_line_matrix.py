'''
This Python file reads the "dot matrices" and converts them to "lines matrices"
'''
#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import os


#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

DECADE_RANGE = range(8, 9)
YEAR_RANGE = range(10)

MATRIX_WIDTH_RANGE = range(1, 120) # Ignore t=1, since all nodes start at 0
MATRIX_LENGTH_RANGE = range(50)


#-------------------------------------------------------------------------------
# Functions
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

# This function transforms all the data (.txt) in one directory to an another
# Parameters:
#   input_folder: specifies the directory that contains subdirectories of data;
#     the subdirectories have names "X0", where X is the decade
#     (e.g. "matrix_50nodes")
#   output_folder: specifies the directory to output the data in subdirectories;
#     the subdirectories have names "X0", where X is the decade
#   function: specifies the transformation for the data,
#     takes in the input directory and filename and returns the output data
def transform_data(
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
        for year in YEAR_RANGE:
            year = str(year)
            filename = decade + year + ".txt"

            # Iterate through all duplicates of the year
            duplicate = 2
            while os.path.isfile(input_dir + filename):
                output = transform_function(
                    input_dir,
                    filename,
                    transform_param
                )
                write_to_file(output_dir, filename, output)

                filename = decade + year + "(" + str(duplicate) + ").txt"
                duplicate += 1

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



#-------------------------------------------------------------------------------
# Scripts
#-------------------------------------------------------------------------------

'''
transform_data(
    "50_nodes/dot_matrix",
    "50_nodes/line_matrix",
    dot_to_line_matrix,
    None
)
plot_data("50_nodes/line_matrix", "50_nodes/line_image", plt.imshow)
'''
'''
transform_data(
    "50_nodes/line_matrix",
    "50_nodes/partial_line_matrix",
    x_year_data_y_year_before_death,
    [5, 5]
)
plot_data(
    "50_nodes/5_death_in_5_years_matrix",
    "50_nodes/partial_line_image",
    plt.imshow
)
'''
'''
transform_data(
    "50_nodes/line_matrix",
    "50_nodes/5_death_in_10_years_matrix",
    x_year_data_y_year_before_death,
    [5, 10]
)
plot_data(
    "50_nodes/5_death_in_10_years_matrix",
    "50_nodes/5_death_in_10_years_image",
    plt.imshow
)
'''
'''
transform_data(
    "matrices/dot_50_annk",
    "matrices/line_50_annk",
    dot_to_line_matrix,
    None
)
'''
transform_data(
    "~/Desktop/Summer Research/cnn/data_sets/training_individuals",
    "~/Desktop/Summer Research/cnn/data_sets/training_individuals/" +
        "5_death_5_years",
    x_year_data_y_year_before_death,
    [5, 5]
)
'''
transform_data(
    "~/Desktop/Summer Research/cnn/data_sets/training_individuals",
    "~/Desktop/Summer Research/cnn/data_sets/training_individuals/" +
        "5_death_10_years",
    x_year_data_y_year_before_death,
    [5, 10]
)
'''
