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
    plot_file("new15.txt")

#-------------------------------------------------------------------------------
# Plot function
#-------------------------------------------------------------------------------

def plot_file(results_name):
    results = tokenize_file(results_name)
    dataSet_list = create_dataSet_list(results)
    dataSet_table = create_dataSet_table(dataSet_list)

    for dataSet_list in dataSet_table:
        print(len(dataSet_list))

def create_dataSet_table(dataSet_list):
    dataSet_table = []
    for dataSet in dataSet_list:
        for i in range(len(dataSet_table)):
            if dataSet.isSameType(dataSet_table[i][0]):
                dataSet_table[i].append(dataSet)
                dataSet = None
        if not dataSet == None:
            dataSet_table.append([dataSet])

    return dataSet_table

def create_dataSet_list(results):
    dataSet = None
    dataSet_list = []

    i = 0
    indices = len(results)
    while i < indices:
        if results[i] == "data":
            i += 1
            dataSet = DataSet(results[i])

        elif results[i] == "history":
            i += 1
            dataSet.history = int(results[i])

        elif results[i] == "global_step":
            i += 1
            dataSet.steps = int(results[i])

            dataSet_list.append(dataSet)

        elif results[i] == "filters":
            i += 1
            dataSet.filters = [int(results[i])]
            i += 1
            while results[i].isdigit():
                dataSet.filters.append(int(results[i]))
                i += 1
            i -= 1

        elif results[i] == "sizes":
            i += 1
            dataSet.filt_sizes = [int(results[i])]
            i += 1
            while results[i].isdigit():
                dataSet.filt_sizes.append(int(results[i]))
                i += 1
            i -= 1

        elif results[i] == "dense":
            i += 1
            dataSet.dense = int(results[i])

        elif results[i] == "logits":
            i += 1
            dataSet.logits = int(results[i])

        elif results[i] == "accuracy":
            i += 1
            dataSet.accuracy = float(results[i])

        elif results[i] == "false":
            i += 1
            if results[i] == "negatives":
                i += 1
                dataSet.false_negative = int(float(results[i]))
            elif results[i] == "positives":
                i += 1
                dataSet.false_positive = int(float(results[i]))

        elif results[i] == "true":
            i += 1
            if results[i] == "positives":
                i += 1
                dataSet.true_positive = int(float(results[i]))
            elif results[i] == "negatives":
                i += 1
                dataSet.true_negative = int(float(results[i]))
        i += 1

    return dataSet_list

def tokenize_file(results_name):
    results_file = open(results_name, "r")
    results = []

    for word in results_file.read().split():
        word = word.replace(",", "").replace("[", "").replace("\'", "")
        word = word.replace("]", "").replace("{", "").replace("}", "")
        word = word.replace(":", "").replace("-", "").replace("/", "")
        if not word == "":
            results.append(word.lower())

    return results

#-------------------------------------------------------------------------------
# Supporting functions
#-------------------------------------------------------------------------------

def avg(x):
    return sum(x) / len(x)

#-------------------------------------------------------------------------------
# Call main
#-------------------------------------------------------------------------------

main()
