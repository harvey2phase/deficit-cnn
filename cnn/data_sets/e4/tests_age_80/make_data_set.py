import numpy as np
import os

output_file = "7_year_history/train_set.txt"
directory1 = "eval_individuals/7_death_5_years/80"
directory2 = "eval_individuals/7_death_10_years/80"

f = open(output_file, "w+")

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
