'''
This Python file reads data from a "X0_all" folder, pick out the 50 most
interesting nodes (from "high_annd_20_most_connected.nodes"), and represent the
data as 50 x 120 matrices

There are two different types of representations:
    1. Lines: Plot 1 for damaged, 0 for health at every time point.
    2. Dots: Plot 1 newly damaged, -1 for newly repaired, and 0 for unchanged
       nodes
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import os.path

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

NODE_COUNT = 100
YEAR_COUNT = 120

DAMAGED = 1
REPAIRED = -1

DATA_DIR = "../raw_data/model_data/e4_by_decade/"
NODE_FILE_DIR = "../raw_data/nodes/100_annk.txt"
MATRIX_OUT_DIR = "../raw_data/matrices/e4/0_annk/dot/"
#IMAGE_OUT_DIR = "images/e4/dot/50_annk/"

DEATH_DECADE_RANGE = range(2, 12)
DEATH_YEAR_RANGE = range(10)

# The information of the nodes of interest
NODES = np.loadtxt(
    NODE_FILE_DIR,
    dtype = {
        'names': ('id', 'deg', 'annk', 'rank'),
        'formats': (np.int32, np.int32, np.int32, np.int32)
    }
)
NODE_ID = NODES['id']
NODE_RANK = NODES['rank']

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

def main():
    make_decade_dot_matrices("8")

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

def create_textfile(filename):

    try:
        f = open(filename + ".txt", "x")

    except FileExistsError:
        count = 2
        while os.path.isfile(filename + "(" + str(count) + ").txt"):
            count += 1
        f = open(filename + "(" + str(count) + ").txt", "x")

    return f


def write_dot_matrix(matrix, filename, death_decade):
    output_dir = MATRIX_OUT_DIR + death_decade + '0/'

    f = open(output_dir + filename + '.txt', "w+")

    for m in matrix:
        f.write(' '.join(map(str, m)) + '\n')

    f.close()


def write_image(matrix, filename, death_decade):
    output_dir = IMAGE_OUT_DIR + death_decade + '0/'

    plt.imshow(matrix)
    plt.xlabel('Time (year)')
    plt.ylabel('Node \"ID\"')
    plt.savefig(output_dir + filename)
    plt.clf()


def make_dot_matrix(filename, death_decade):

    input_dir = DATA_DIR + death_decade + '0/'

    # The deficit information of an individual
    individual = np.loadtxt(
        input_dir + filename + '.txt',
        dtype = {
            'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)
        }
    )
    ind_time = individual['time']
    ind_node_id = individual['id']
    ind_state = individual['state']

    change_range = range(len(ind_node_id))

    matrix = np.full((NODE_COUNT, YEAR_COUNT), 0)

    # Iterate through all damages/repairs in an individual
    for i in change_range:

        # Pick out the nodes of interest
        if ind_node_id[i] in NODE_ID:

            # Find the damaged/repaired index of the matrix
            # (based on node ID and time)
            rank = NODE_RANK[np.where(NODE_ID == ind_node_id[i])[0][0]] - 1
            time = ind_time[i]

            if ind_state[i] == 1:
                matrix[rank][time] = DAMAGED
            else:
                matrix[rank][time] = REPAIRED

    write_dot_matrix(matrix, filename, death_decade)
    #write_image(matrix, filename, death_decade)

# Takes in a String that is a digit that represents the decade (folder) to plot
def make_decade_dot_matrices(death_decade):

    input_dir = DATA_DIR + death_decade + '0/'

    for death_year in DEATH_YEAR_RANGE:
        death_year = str(death_year)
        filename = death_decade + death_year

        duplicate = 2
        while os.path.isfile(input_dir + filename + ".txt"):
            print(filename + ".txt")

            make_dot_matrix(filename, death_decade)

            filename = death_decade + death_year
            filename += '(' + str(duplicate) + ')'

            duplicate += 1

def make_all_dot_matrices():

    # Iterate through all 12 decades of death ages
    for i in DEATH_DECADE_RANGE:
        make_decade_dot_matrices(str(i))
#-------------------------------------------------------------------------------
# Call main
#-------------------------------------------------------------------------------

main()
