import numpy as np
import matplotlib.pyplot as plt

def prob_death_age():
    raw_death_age = np.loadtxt('Code/Data/RawDeathAgeDataID1Gammap7.5Gamman6.5N10000Number1000R3.0nd2Alpha2.27AvgDeg4ANDSingleSingleSeed1ScaleFreepA0.0')
    death_year = np.loadtxt('Code/Data/DeathAgeYear.txt')
    death_year = np.sort(death_year)

def prob_degrees():
    network_degrees = 'Code/Data/NetworkDegreesGammap7.5Gamman6.5N10000Number1000R3.0nd2Alpha2.27AvgDeg4ANDSingleSingleSeed1ScaleFreepA0.0'

def prob_deficits():
    raw_deficits = np.loadtxt('Data/RawDeficitsID1Gammap7.5Gamman6.5N10000Number1000R3.0nd2Alpha2.27AvgDeg4ANDSingleSingleSeed1ScaleFreepA0.0')
    node_id = raw_deficits[:, 1]
    time = raw_deficits[:, 0] / 0.00183
    plt.scatter(time, node_id, s = 0.05)

#plt.plot(death_age / 0.00183)



#plt.scatter(np.linspace(1, 1000, 1000), death_year)
prob_deficits()
plt.show()
#plt.savefig('deficits col0 vs col1', dpi = 1000)
