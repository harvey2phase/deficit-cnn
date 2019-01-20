import numpy as np
import os.path.isfile

gamma_0 = 0.00183       # (unit: per year) divide to get year.

death_year = np.loadtxt("death_year.1")
raw_deficits = np.loadtxt("raw_deficits.0")

# The three columns in file "raw_deficits"
change_time = raw_deficits[:, 0] / gamma_0
node_id = raw_deficits[:, 1]
state = raw_deficits[:, 2]


#min_death = min(death_year)

year = 0
f = create_textfile(death_year[year])

for change in range(0, len(change_time - 1)):
    if change_time[change + 1] - change_time[change] < 0:
        year += 1
        f.close()
        f = create_textfile(death_year[year])
    f.write(str(change_time[change]) + "\t" + str(node_id[change]) + "\t")
    f.write(str(state[change]) + "\n")

f.write(str(change_time[len(change_time)]) + "\t" + str(node_id[len(node_id)]))
f.write("\t" + str(state[len(state)]) + "\n")
f.close()

def create_textfile(filename):
    filename = "individual_data/" + str(filename)
    try:
        f = open(filename + ".1", "x")

    except FileExistsError:
        count = 2
        while isfile(filename + "(" + str(count) + ").1"):
            count += 1
        f = open(filename + "(" + str(count) + ").1", "x")

    return f
