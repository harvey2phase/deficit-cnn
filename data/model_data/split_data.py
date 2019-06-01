#-------------------------------------------------------------------------------
# Imports and constants
#-------------------------------------------------------------------------------

import numpy as np
import os

gamma_0 = 0.00183       # (unit: per year) divide to get year.

#-------------------------------------------------------------------------------
# File directories setup
#-------------------------------------------------------------------------------

output_folder = "e5_all/"
death_year_filename = "e5_death_year.txt"
raw_deficits_filename = "../../spencer_code/Data/"
raw_deficits_filename += "RawDeficitsID1Gammap7.5Gamman6.5N10000Number10000"

#-------------------------------------------------------------------------------
# Supporting functions
#-------------------------------------------------------------------------------

def create_textfile(filename):
    filename = output_folder + str(int(filename))
    try:
        f = open(filename + ".txt", "x")

    except FileExistsError:
        count = 2
        while os.path.isfile(filename + "(" + str(count) + ").txt"):
            count += 1
        f = open(filename + "(" + str(count) + ").txt", "x")

    return f

#-------------------------------------------------------------------------------
# Scripts to split raw deficits
#-------------------------------------------------------------------------------

death_year = np.loadtxt(death_year_filename)
raw_deficits = np.loadtxt(raw_deficits_filename)

# The three columns in file "raw_deficits"
change_time = raw_deficits[:, 0] / gamma_0
node_id = raw_deficits[:, 1]
state = raw_deficits[:, 2]

raw_length = len(change_time) - 1


year = 0
f = create_textfile(death_year[year])

for change in range(0, raw_length - 1):
    f.write(str(change_time[change]) + "\t" + str(int(node_id[change])) + "\t")
    f.write(str(int(state[change])) + "\n")
    if change_time[change + 1] - change_time[change] < 0:
        year += 1
        f.close()
        f = create_textfile(death_year[year])

f.write(str(change_time[raw_length]) + "\t")
f.write(str(int(node_id[raw_length])))
f.write("\t" + str(int(state[raw_length])) + "\n")
f.close()
