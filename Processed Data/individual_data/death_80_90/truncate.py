import numpy as np

def truncate_file(filename):
    deficits = np.loadtxt(filename,
        dtype = {'names': ('time', 'id', 'state'),
            'formats': (np.int32, np.int32, np.int32)})
    #f = open(filename, 'w')
    for d in deficits:
        if d['id'] in degrees:
            print(d)

    #print(deficits)
    #f.close()

degrees = np.loadtxt("ten_most_connected.txt",
        usecols = (0,))

truncate_file('80.txt')
'''
for i in range (10):
    filename = '8' + str(i)
    while os.path.isfile(filename + '.txt'):
        count = 2
        truncate_file(filename)
        filename = '8' + str(i) + '(' + str(count) + ')'
'''

#print(degrees)
