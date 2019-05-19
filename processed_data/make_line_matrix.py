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

INPUT_FOLDER = "dot_matrix_50nodes/"
OUTPUT_FOLDER = "line_matrix_50nodes/"

DECADE_RANGE = range(2, 12)
YEAR_RANGE = range(10)

MATRIX_WIDTH_RANGE = range(1, 120) # Ignore t=1, since all nodes start at 0
MATRIX_LENGTH_RANGE = range(50)


#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

def dot_to_line_matrix(input_folder, filename):
    matrix = np.loadtxt(input_folder + filename)
    length_range = range(len(matrix))
    width_range = range(len(matrix[0]))     #range(0, 120)
    for w in MATRIX_WIDTH_RANGE:
        if w > int(filename[0] + filename[1], 10):
            for l in MATRIX_LENGTH_RANGE:
                matrix[l][w] = -2
            break
        for l in MATRIX_LENGTH_RANGE:
            if (matrix[l][w] == 0):
                matrix[l][w] = matrix[l][w-1]
            elif (matrix[l][w] == -1):
                matrix[l][w] = 0

    return matrix

# This function takes in an output 2D matrix, then writes the matrix to the
# file (creates the file if it does not exist).
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
def transform_data(input_folder, output_folder, transform_function):
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
                output = transform_function(input_dir, filename)
                write_to_file(output_dir, filename, output)

                filename = decade + year + "(" + str(duplicate) + ").txt"
                duplicate += 1

# This function takes in a data folder and plot the data inside it to a plot
# folder
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

# TODO
# Truncate to line images to X year-period health state Y years before death
# Somehow differentiate data for forty year olds and 80 year olds
# (Maybe use 4 for damaged for age 40 and 8 for eighty instead of all 1)

#-------------------------------------------------------------------------------
# Scripts
#-------------------------------------------------------------------------------

transform_data("matrix_50nodes", "line_matrix_50nodes", dot_to_line_matrix)
plot_data("line_matrix_50nodes", "line_image_50nodes", plt.imshow)
