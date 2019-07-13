import numpy as np

#-------------------------------------------------------------------------------
# Constants and global variables
#-------------------------------------------------------------------------------

deg_filename = "network_degrees_degrees.txt"
annk_filename = "network_degrees_ANNK.txt"

COUNT = 1

#-------------------------------------------------------------------------------
# Supporting functions
#-------------------------------------------------------------------------------

def load_net_deg(filename):
    return np.loadtxt(
        filename,
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
    global COUNT
    output_file.write(
        str(line["id"]) + "\t" +
        str(line["deg"]) + "\t" +
        str(line["annk"]) + "\t" +
        str(COUNT) + "\n"
    )
    COUNT += 1

def make_decreasing_annk_list(output_filename, deg_count, annk_count):
    highest_deg = load_net_deg(deg_filename)[-deg_count :]
    highest_deg.sort(order = 'annk')
    highest_deg = highest_deg[::-1]

    highest_annk = load_net_deg(annk_filename)[-annk_count :]

    output_file = open(output_filename, "w+")
    for line in highest_annk:
        write_line(output_file, line)
    for line in highest_deg:
        write_line(output_file, line)
    output_file.close()

#-------------------------------------------------------------------------------
# Scripts
#-------------------------------------------------------------------------------

make_decreasing_annk_list("60_annk.txt", 30, 30)
COUNT = 1
make_decreasing_annk_list("80_annk.txt", 40, 40)
COUNT = 1
make_decreasing_annk_list("100_annk.txt", 50, 50)
