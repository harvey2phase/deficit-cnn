# Dicretizes time to integers and select the tem most connected nodes

import numpy as np
import matplotlib.pyplot as plt
import os.path

input_dir = 'death_80_90_truncated/'
output_dir = 'death_80_90_plot/'

def plot(filename):
    deficits = np.loadtxt(input_dir + filename,
        dtype = {'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)})
    time, node, state = deficits['time'], deficits['id'], deficits['state']

    for i in range(len(time)):
        if state[i] == 1:
            plt.scatter(time[i], node[i], c = 'red')
        else:
            plt.scatter(time[i], node[i], c = 'green')

    plt.xlabel('Time (year)')
    plt.ylabel('Node ID')
    plt.savefig(output_dir + filename)


plot('80.txt')

'''
for i in range(10):
    filename = "8" + str(i)
    count = 2
    while os.path.isfile(input_dir + filename + ".txt"):
        print(filename + ".txt")
        truncate_file(filename + ".txt")
        filename = '8' + str(i) + '(' + str(count) + ')'
        count += 1
'''
