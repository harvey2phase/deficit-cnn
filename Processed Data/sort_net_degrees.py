import numpy as np

degrees = np.loadtxt("network_degrees.txt",
        dtype = {'names': ('id', 'deg', 'ANND'),
            'formats': (np.int, np.int, np.float)})

degrees.sort(order = 'deg')

#print(degrees)
i = 9999
while i > 9989:
    print(degrees[i]['id'], degrees[i]['deg'], degrees[i]['ANND'])
    i -= 1
