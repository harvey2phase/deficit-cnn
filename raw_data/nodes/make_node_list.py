import numpy as np

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

deg_filename = "network_degrees.txt"
deg_count = 30
annd_count = 30
output_filename = "60_annk_nodes.txt"

#-------------------------------------------------------------------------------
# Script
#-------------------------------------------------------------------------------

degrees = np.loadtxt(
    deg_filename,
    dtype = {
        'names': ('id', 'deg', 'ANND'),
        'formats': (np.int, np.int, np.float)}
)
degrees.sort(order = ['deg', 'ANND'])

count = 1
output = open(output_filename, "w+")
for line in degrees[: -10000 + deg_count]:
    print(
        line['id'] + "\t" + str(line['deg']) + "\t" + str(line['ANND']) + "\t" + str(count)
    )
    count += 1
output.close()

output = open(output_filename, "a")
for line in degrees[10000 - deg_count:]:
    print(
        line['id'] + "\t"
        + str(line['deg']) + "\t"
        + str(line['ANND']) + "\t"
        + str(count)
    )
    count += 1

output.close()
