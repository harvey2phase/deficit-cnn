from DataSet import DataSet

import numpy as np
import matplotlib.pyplot as plt
import os

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

HIS = []
AC = []
LAB = []

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

def main():
    plot_file("10x|e5st|32_64f|5_5_5_5si|256d|2l", 10)
    '''
    for filename in os.listdir("."):
        if filename[-4:] == ".txt":
            filename = filename[:-4]
            i = 0
            his = ""
            while filename[i].isdigit():
                his += filename[i]
                i += 1
            plot_file(filename, int(his))

    fig, ax = plt.subplots()
    ax.scatter(HIS, AC)
    for i, lab in enumerate(LAB):
        ax.annotate(lab, (HIS[i], AC[i]))

    plt.show()
    '''

#-------------------------------------------------------------------------------
# Plot function
#-------------------------------------------------------------------------------

def plot_file(results_name, his):

    results_file = open(results_name + ".txt", "r")
    results = []

    for word in results_file.read().split():
        word = word.replace(",", "").replace("[", "").replace("\'", "")
        word = word.replace("]", "").replace("{", "").replace("}", "")
        word = word.replace(":", "").replace("-", "").replace("/", "")
        if not word == "":
            results.append(word.lower())

    for r in results:
        print(r)

    indices = len(results)
    accuracy = []
    true_positive = []
    false_negative = []
    true_negative = []
    false_positive = []

    i = 0
    while i < indices:
        if results[i] == "data":
            i += 1
            dataSet = DataSet(results[i])

            while not results[i] == "history": i += 1
            i += 1
            dataSet.history = int(results[i])

            while not results[i] == "accuracy": i += 1
            i += 1
            dataSet.accuracy = float(results[i])

            while not results[i] == "false": i += 1
            while not results[i] == "negatives": i += 1
            i += 1
            dataSet.false_negative = int(float(results[i]))
            while not results[i] == "positives": i += 1
            i += 1
            dataSet.false_positive = int(float(results[i]))

            while not results[i] == "true": i += 1
            while not results[i] == "positives": i += 1
            i += 1
            dataSet.true_positive = int(float(results[i]))
            while not results[i] == "negatives": i += 1
            i += 1
            dataSet.true_negative = int(float(results[i]))
        i += 1

    accuracy = np.array(accuracy)
    true_positive = np.array(true_positive)
    false_negative = np.array(false_negative)
    true_negative = np.array(true_negative)
    false_positive = np.array(false_positive)

    HIS.append(his)
    #AC.append(avg(accuracy))

    while results_name[0] != "|":
        results_name = results_name[1:]
    LAB.append(str(len(accuracy)) + results_name)

    #print("accuracy: ", accuracy)
    #print("true positive: ", true_positive)
    #print("false negative: ", false_negative)
    #print("true negative: ", true_negative)
    #print("false positive: ", false_positive)
    #print("Sanity check: ", true_positive + false_negative)
    #print("Sanity check: ", true_negative + false_positive)

#-------------------------------------------------------------------------------
# Supporting functions
#-------------------------------------------------------------------------------

def avg(x):
    return sum(x) / len(x)

#-------------------------------------------------------------------------------
# Call main
#-------------------------------------------------------------------------------

main()
