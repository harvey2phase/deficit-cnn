import numpy as np
import os

f = open("eval_set_80.txt", "w+")

directory = "eval_individuals/5_death_5_years/80"
for filename in os.listdir(directory):
    if filename[0] == '8':
        matrix = np.loadtxt(directory + "/" +  filename)

        for row in matrix:
            for state in row:
                if state != 0:
                    state = 1
                f.write(str(state) + " ")
        f.write("\n")

directory = "eval_individuals/5_death_10_years/80"
for filename in os.listdir(directory):
    if filename[0] == '8':
        matrix = np.loadtxt(directory + "/" +  filename)

        for row in matrix:
            for state in row:
                if state != 0:
                    state = 1
                f.write(str(state) + " ")
        f.write("\n")

f.close()
