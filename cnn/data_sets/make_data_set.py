import numpy as np
import os

f = open("7_eval_80.txt", "w+")

directory1 = "eval_individuals/7_death_5_years/80"
directory2 = "eval_individuals/7_death_10_years/80"

for filename in os.listdir(directory1):
    if filename[0] == '8':
        matrix = np.loadtxt(directory + "/" +  filename)

        for row in matrix:
            for state in row:
                if state != 0:
                    state = 1
                f.write(str(state) + " ")
        f.write("\n")

for filename in os.listdir(directory2):
    if filename[0] == '8':
        matrix = np.loadtxt(directory + "/" +  filename)

        for row in matrix:
            for state in row:
                if state != 0:
                    state = 1
                f.write(str(state) + " ")
        f.write("\n")

f.close()
