import numpy as np
import matplotlib.pyplot as plt

death_age = 22

filename = str(death_age) + '.txt'

ind = np.loadtxt(path + filename)

time = np.array(ind[:, 0], int)
node = np.array(ind[:, 1], int)
state = np.array(ind[:, 2], int)

# Discretize time to 1 year and make a 2D image of node health vs. time
image_length = death_age + 1
image = np.zeros((image_length, 10000))
year = 0
year_end = 1

for i in range(len(time)):
    image[time[i]][node[i]] = state[i]

for year in range(image_length):
    for node in range(10000):
        if image[year][node] == 1:
            plt.scatter(year, node, c = 'red')
        else:
            plt.scatter(year, node, c = 'green')
