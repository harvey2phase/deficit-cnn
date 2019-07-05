import numpy as np

from transforms import transform_and_write

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

MATRIX_LENGTH_RANGE = range(50)

#-------------------------------------------------------------------------------
# Transformations
#-------------------------------------------------------------------------------

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
