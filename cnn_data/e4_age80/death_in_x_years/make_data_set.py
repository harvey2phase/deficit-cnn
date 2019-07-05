import numpy as np
import os

output_file = "7_year_history/eval_set.txt"
directory1 = "7_year_history/eval/death_in_5"
directory2 = "7_year_history/eval/death_in_12"

f = open(output_file, "w+")

for filename in os.listdir(directory1):
    if filename[0] == '8':
        matrix = np.loadtxt(directory1 + "/" +  filename)

        for row in matrix:
            for state in row:
                if state != 0:
                    state = 1
                f.write(str(state) + " ")
        f.write("\n")

for filename in os.listdir(directory2):
    if filename[0] == '8':
        matrix = np.loadtxt(directory2 + "/" +  filename)

        for row in matrix:
            for state in row:
                if state != 0:
                    state = 1
                f.write(str(state) + " ")
        f.write("\n")

f.close()
