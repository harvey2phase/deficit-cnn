from transforms import transform_and_write

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