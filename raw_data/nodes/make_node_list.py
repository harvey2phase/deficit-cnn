import numpy as np

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

deg_filename = "network_degrees_degrees.txt"
annk_filename = "network_degrees_ANNK.txt"
deg_count = 10
annd_count = 10
output_filename = "60_annk_nodes.txt"

COUNT = 1

#-------------------------------------------------------------------------------
# Script
#-------------------------------------------------------------------------------

def load_net_deg(filename):
    return np.loadtxt(
        deg_filename,
        dtype = {
            "names": ("id", "deg", "annk"),
            "formats": (np.int, np.int, np.float)
        }
    )

def print_line(line):
    global COUNT
    print(
        str(line["id"]) + "\t" +
        str(line["deg"]) + "\t" +
        str(line["annk"]) + "\t" +
        str(COUNT)
    )
    COUNT += 1

def write_line(output_file, line):
    output_file.write(
        str(line["id"]) + "\t" +
        str(line["deg"]) + "\t" +
        str(line["annk"]) + "\n"
    )

#-------------------------------------------------------------------------------
# Script
#-------------------------------------------------------------------------------

highest_deg = load_net_deg(deg_filename)[: -10000 + deg_count]
highest_annk = load_net_deg(annk_filename)[-10000 + deg_count :]

for line in highest_deg:
    print_line(line)


#output_file = open(out_filename, "w+")
#for line in highest_deg:
#    write_line(output_file, line)
#output_file.close()

'''
highest_deg.sort(order = "annk")
for line in highest_deg:
    print_line(line)
print("---")

highest_annd = load_net_deg("annk")#[10000 - deg_count]
for line in highest_annd:
    print_line(line)
'''

#output = open(output_filename, "w+")
#output = open(output_filename, "a")
#output.close()

