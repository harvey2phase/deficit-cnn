# Converts raw death age to death age in unit years

import numpy as np

raw_filename = "../../spencer_code/Data/"
raw_filename += "RawDeathAgeDataID1Gammap7.5Gamman6.5N10000Number100000R3."
raw_filename += "0nd2Alpha2.27AvgDeg4ANDSingleSingleSeed1ScaleFreepA0.0"

year_filename = "e5_death_year.txt"
gamma_0 = 0.00183       # (unit: per year) divide to get year

raw = np.loadtxt(raw_filename)

years = raw / gamma_0

year_file = open(year_filename, "w+")

for year in years:
    year_file.write(str(year) + "\n")

year_file.close()
