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

WIDTH_RANGE = range(1, 120) # Ignore t=1, since all nodes start at 0
LENGTH = range(50)


#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

def dot_to_line_matrix(input_folder, filename):
    matrix = np.loadtxt(input_folder + filename)
    length_range = range(len(matrix))
    width_range = range(len(matrix[0]))
    for l in length_range:
        for w in width_range:
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

def plot_data()

#-------------------------------------------------------------------------------
# Scripts
#-------------------------------------------------------------------------------

transform_data("matrix_50nodes", "line_matrix_50nodes", dot_to_line_matrix)
