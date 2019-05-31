import numpy as np
import os

f = open("training_set_80.txt", "w")

directory = "5_death_in_5_years_matrix/80"
for filename in os.listdir(directory):
    matrix = np.loadtxt(directory + "/" +  filename)

    for row in matrix:
        for state in row:
            if state != 0:
                state = 1
            f.write(str(state) + " ")
    f.write("\n")

directory = "5_death_in_10_years_matrix/80"
for filename in os.listdir(directory):
    matrix = np.loadtxt(directory + "/" +  filename)

    for row in matrix:
        for state in row:
            if state != 0:
                state = 1
            f.write(str(state) + " ")
    f.write("\n")

f.close()
