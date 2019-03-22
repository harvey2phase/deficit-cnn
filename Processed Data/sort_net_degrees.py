import numpy as np

degrees = np.loadtxt("network_degrees.txt",
        dtype = {'names': ('id', 'deg', 'ANND'),
            'formats': (np.int, np.int, np.float)})

#degrees.sort(order = 'deg')
degrees.sort(order = 'ANND')

i = 9999
count = 1
while i > 9979:
    print(str(degrees[i]['id']) + "\t" + str(degrees[i]['deg'])
            + "\t" + str(degrees[i]['ANND']) + "\t" + str(count))
    i -= 1
    count += 1
