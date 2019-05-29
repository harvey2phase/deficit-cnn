import numpy as np
import os

directory = "5_death_in_10_years_matrix/80"
count = 0
f = open("training_set_80.txt", "w")
for filename in os.listdir(directory):
    print(filename)
    matrix = np.loadtxt(directory + "/" +  filename)

    for row in matrix:
        for state in row:
            if state != 0:
                state = 1
            f.write(str(state) + " ")
    f.write("\n")
