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

# The information of the nodes of interest
nodes = np.loadtxt("high_annd_20_most_connected.nodes",
        dtype = {'names': ('id', 'conn', 'ANNC', 'rank'),
            'formats': (np.int32, np.int32, np.int32, np.int32)})
node_id, node_rank = nodes['id'], nodes['rank']

node_count, year_count = 50, 120

def create_textfile(filename):

    try:
        f = open(filename + ".txt", "x")

    except FileExistsError:
        count = 2
        while os.path.isfile(filename + "(" + str(count) + ").txt"):
            count += 1
        f = open(filename + "(" + str(count) + ").txt", "x")

    return f

def make_dot_matrix(filename, input_dir, output_dir):

    # The deficit information of an individual
    individual = np.loadtxt(input_dir + filename + '.txt',
        dtype = {'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)})
    ind_time = individual['time']
    ind_node_id = individual['id']
    ind_state = individual['state']

    r = len(ind_node_id)

    matrix = np.full((node_count, year_count), 0)

    # Iterate through all damages/repairs in an individual
    for i in range(r):

        # Pick out the nodes of interest
        if ind_node_id[i] in node_id:

            rank = node_rank[np.where(node_id == ind_node_id[i])[0][0]] - 1

            # Find the position in the matrix, based on time and node ID,
            # and chage its value, based on damaged/repaired
            if ind_state[i] == 1:
                matrix[rank][ind_time[i]] = 1
            else:
                matrix[rank][ind_time[i]] = -1

    f = open(filename + '.txt', 'x')

    plt.imshow(matrix)
    plt.xlabel('Time (year)')
    plt.ylabel('Node \"ID\"')
    plt.savefig(output_dir + filename)
    plt.clf()

def plot_decade(death_decade):

    input_dir = death_decade
    input_dir += '0_all/'

    output_dir = 'deg_annd_' + death_decade + '0/'
    output_dir += death_decade
    output_dir += '0/'

    for i in range(10):
        filename = death_decade
        filename += str(i)

        count = 2
        while os.path.isfile(input_dir + filename + ".txt"):
            print(filename + ".txt")
            plot(filename, input_dir, output_dir)

            filename = death_decade
            filename += str(i)
            filename += '(' + str(count) + ')'

            count += 1

def main():

    for i in range(12):
        plot_decade(str(i))

#main()
make_dot_matrix('80', '80_all/', 'hi')
