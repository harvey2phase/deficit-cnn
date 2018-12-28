import numpy as np
import matplotlib.pyplot as plt

file2 = np.loadtxt("Code/Data/RawDeficitsID1Gammap7.5Gamman6.5N10000Number1000R3.0nd2Alpha2.27AvgDeg4ANDSingleSingleSeed1ScaleFreepA0.0")

for f in file2[0]:
    print(f)
plt.plot(file2[0])
plt.savefig('deficit column 0', dpi = 1000)
