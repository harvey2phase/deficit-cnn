import numpy as np
import matplotlib.pyplot as plt

file2 = np.loadtxt("Data/RawDeficitsID1Gammap7.5Gamman6.5N10000Number1000R3.0nd2Alpha2.27AvgDeg4ANDSingleSingleSeed1ScaleFreepA0.0")

plt.plot(file2)
plt.show()
