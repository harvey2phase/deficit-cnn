# Dicretizes time to integers and select the tem most connected nodes

import numpy as np
import os.path

input_dir = 'death_80_90/'
output_dir = 'death_80_90_truncated/'

def truncate_file(filename):
    deficits = np.loadtxt(input_dir + filename,
        dtype = {'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)})

    f = open(output_dir + filename, 'x')

    for d in deficits:
        if d['id'] in degrees:
            f.write(str(d['time']) + "\t" +  str(d['id'])
                    + "\t" + str(d['state']) + "\n")

    f.close()

degrees = np.loadtxt("ten_most_connected.txt",
        usecols = (0,))

#truncate_file('80.txt')

for i in range(10):
    filename = "8" + str(i)
    count = 2
    while os.path.isfile(input_dir + filename + ".txt"):
        print(filename + ".txt")
        truncate_file(filename + ".txt")
        filename = '8' + str(i) + '(' + str(count) + ')'
        count += 1
