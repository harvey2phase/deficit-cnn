#-------------------------------------------------------------------------------
# Imports and constants
#-------------------------------------------------------------------------------

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

    # Iterate through all the files in the input folder
    for filename in os.listdir(input_folder):
        print(filename)
        output = transform_function(
            input_folder,
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