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
    plot_file("\'10x|e5st|32_64f|5_5_5_5si|256d|2l.txt\'")
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
    results_list = []

    for word in results_file.read().split():
        word = word.replace(",", "").replace("[", "").replace("\'", "")
        word = word.replace("]", "").replace("{", "").replace("}", "")
        word = word.replace(":", "").replace("-", "")
        if not word == "":
            results_list.append(word)

    indices = range(len(results_list))
    accuracy = []
    true_positive = []
    false_negative = []
    true_negative = []
    false_positive = []

    for i in indices:
        if results_list[i] == "accuracy":
            i += 1
            accuracy.append(float(results_list[i]))
        elif results_list[i] == "true":
            i += 1
            if results_list[i] == "positives":
                i += 1
                true_positive.append(int(float(results_list[i])))
            elif results_list[i] == "negatives":
                i += 1
                true_negative.append(int(float(results_list[i])))
        elif results_list[i] == "false":
            i += 1
            if results_list[i] == "positives":
                i += 1
                false_positive.append(int(float(results_list[i])))
            elif results_list[i] == "negatives":
                i += 1
                false_negative.append(int(float(results_list[i])))

    accuracy = np.array(accuracy)
    true_positive = np.array(true_positive)
    false_negative = np.array(false_negative)
    true_negative = np.array(true_negative)
    false_positive = np.array(false_positive)

    HIS.append(his)
    AC.append(avg(accuracy))

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
