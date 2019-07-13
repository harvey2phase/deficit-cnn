from transforms import transform_and_write

import numpy as np

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

MATRIX_WIDTH_RANGE = range(1, 120) # Ignore t=1, since all nodes start at 0
MATRIX_LENGTH_RANGE = range(100)

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

def main():
    transform_and_write(
        "../raw_data/matrices/e4/100_annk/dot",
        "../raw_data/matrices/e4/100_annk/line",
        dot_to_line_matrix,
        None
    )

#-------------------------------------------------------------------------------
# Dot to line matrix function
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

#-------------------------------------------------------------------------------
# Call main
#-------------------------------------------------------------------------------

main()
