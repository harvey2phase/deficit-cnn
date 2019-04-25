'''
This Python file reads a "X0_all" folder and plot the damage/repair state of
the 20 nodes with the highest average nearest neighbour degree (ANND)

If a node is damaged at time t, it is represented on the scatter plot as a red
dot; if it repaired, a green dot is used instead

The y-axis is the rank of the ANND, i.e. y = 1 is the node with the highest ANND
'''

import numpy as np
import matplotlib.pyplot as plt
import os.path

def plot(filename, input_dir, output_dir, id_deg):
    deficits = np.loadtxt(input_dir + filename + '.txt',
        dtype = {'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)})
    time, node, state = deficits['time'], deficits['id'], deficits['state']

    for i in range(len(time)):
        if node[i] in id_deg:
            if state[i] == 1:
                plt.scatter(time[i],
                        id_deg[np.where(id_deg == node[i])[0][0]],
                        c = 'red')
            else:
                plt.scatter(time[i],
                        id_deg[np.where(id_deg == node[i])[0][0]],
                        c = 'green')

    plt.xlabel('Time (year)')
    plt.ylabel('Node ID')
    plt.xlim(-5, 120)
    plt.ylim(-500, 10500)
    plt.savefig(output_dir + filename)
    plt.clf()

def plot_decade(death_decade):

    input_dir = death_decade + '0_all/'
    output_dir = 'annd_' + death_decade + '0/'

    degrees = np.loadtxt("highest_annd.txt",
            dtype = {'names': ('id', 'conn', 'ANNC', 'rank'),
                'formats': (np.int32, np.int32, np.int32, np.int32)})
    id_deg = degrees['id']

    for i in range(10):
        filename = death_decade + str(i)
        count = 2
        while os.path.isfile(input_dir + filename + ".txt"):
            print(filename + ".txt")
            plot(filename, input_dir, output_dir, id_deg)
            filename = death_decade + str(i) + '(' + str(count) + ')'
            count += 1

def main():
    for i in range(12):
        plot_decade(str(i))

main()
