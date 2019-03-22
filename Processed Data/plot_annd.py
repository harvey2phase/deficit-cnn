# Dicretizes time to integers and select the tem most connected nodes

import numpy as np
import matplotlib.pyplot as plt
import os.path

death_decade = "9"

input_dir = death_decade + '0_all/'
output_dir = 'plot_' + death_decade + '0_20_nodes_rank/'

degrees = np.loadtxt("20_most_connected.txt",
        dtype = {'names': ('id', 'conn', 'ANNC', 'rank'),
            'formats': (np.int32, np.int32, np.int32, np.int32)})
id_deg, rank_deg = degrees['id'], degrees['rank']

def plot(filename):
    deficits = np.loadtxt(input_dir + filename + '.txt',
        dtype = {'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)})
    time, node, state = deficits['time'], deficits['id'], deficits['state']

    for i in range(len(time)):
        if node[i] in id_deg:
            if state[i] == 1:
                plt.scatter(time[i],
                        rank_deg[np.where(id_deg == node[i])[0][0]],
                        c = 'red')
            else:
                plt.scatter(time[i],
                        rank_deg[np.where(id_deg == node[i])[0][0]],
                        c = 'green')

    plt.xlabel('Time (year)')
    plt.ylabel('Node rank')
    plt.xlim(-5, 95)
    plt.ylim(-5, 25)
    plt.savefig(output_dir + filename)
    plt.clf()


for i in range(10):
    filename = death_decade + str(i)
    count = 2
    while os.path.isfile(input_dir + filename + ".txt"):
        print(filename + ".txt")
        plot(filename)
        filename = death_decade + str(i) + '(' + str(count) + ')'
        count += 1
