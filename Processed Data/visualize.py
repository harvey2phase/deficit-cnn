import matplotlib.pyplot as plt
import numpy as np

def scatter(time, node, state):
    for i in range(0, len(time)):
        if state[i] == 1:
            plt.scatter(time[i], node[i], c = 'red', s = 0.5)
        elif state[i] == 0:
            plt.scatter(time[i], node[i], c = 'green', s = 0.7)
        else:
            print("WHAT THE")

def deficit_total_dam_discrete_time(time, node, state):
    t0, total_dam, dam, rep = 1, 0, 0, 0
    times, total_dams, dams, reps = [], [], [], []
    for i in range(0, len(time)):
        if time[i] > t0:
            times.append(t0)
            total_dams.append(total_dam)
            dams.append(dam)
            reps.append(rep)

            t0 += 1
            dam = 0
            rep = 0

        if state[i] == 1:
            total_dam += 1
            dam += 1
        elif state[i] == 0:
            total_dam -= 1
            rep += 1
        else:
            print("WHAT THE")

    plt.xlabel("Discrete time (year)")
    plt.ylabel("Number of damaged nodes")
    plt.yscale("log")
    plt.plot(times, total_dams, c = 'b')
    plt.plot(times, dams, c = 'r')
    plt.plot(times, reps, c = 'g')

def both(time, node, state):
    plt.figure(1)

    t0, total_dam, dam, rep = 1, 0, 0, 0
    times, total_dams, dams, reps = [], [], [], []
    for i in range(0, len(time)):
        if time[i] > t0:
            times.append(t0)
            total_dams.append(total_dam)
            dams.append(dam)
            reps.append(rep)

            t0 += 1
            dam = 0
            rep = 0

        if state[i] == 1:
            plt.scatter(time[i], node[i], c = 'red', s = 0.7)

            total_dam += 1
            dam += 1

        elif state[i] == 0:
            plt.scatter(time[i], node[i], c = 'green', s = 1)

            total_dam -= 1
            rep += 1

    plt.xlabel("Time (year)")
    plt.ylabel("Node ID")

    plt.figure(2)

    plt.xlabel("Discrete time (year)")
    plt.ylabel("Number of damaged nodes")
    plt.yscale("log")
    plt.plot(times, total_dams, c = 'b')
    plt.plot(times, dams, c = 'r')
    plt.plot(times, reps, c = 'g')

    plt.figure(3)

    plt.xlabel("Discrete time (year)")
    plt.ylabel("Number of damaged nodes")
    plt.plot(times, total_dams, c = 'b')
    plt.plot(times, dams, c = 'r')
    plt.plot(times, reps, c = 'g')

ind = np.loadtxt("individual_data/69.txt")

time = ind[:, 0]
node = ind[:, 1]
state = ind[:, 2]

#plt.figure(1)
#scatter(time, node, state)
#plt.figure(2)
#deficit_total_dam_discrete_time(time, node, state)

both(time, node, state)

plt.show()
