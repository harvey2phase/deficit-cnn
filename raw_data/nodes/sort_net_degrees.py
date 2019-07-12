import numpy as np

deg = np.loadtxt(
    "network_degrees.txt",
    dtype = {
        'names': ('id', 'deg', 'ANND'),
        'formats': (np.int, np.int, np.float)}
).sort(order = 'deg')

annd = np.loadtxt(
    "network_degrees.txt",
    dtype = {
        'names': ('id', 'deg', 'ANND'),
        'formats': (np.int, np.int, np.float)}
).sort(order = 'ANND')

i = 9999
count = 1
while i > 9979:
    print(str(degrees[i]['id']) + "\t" + str(degrees[i]['deg'])
            + "\t" + str(degrees[i]['ANND']) + "\t" + str(count))
    i -= 1
    count += 1
