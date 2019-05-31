# Converts raw death age to death age in unit years

import numpy as np

raw_filename = "e4_raw_death_age.txt"
year_filename = "e4_death_year.txt"
gamma_0 = 0.00183       # (unit: per year) divide to get year

raw = np.loadtxt(raw_filename)
years = raw / gamma_0

year_file = open(year_filename, "w+")

for year in years:
    year_file.write(str(year) + "\n")

year_file.close()
