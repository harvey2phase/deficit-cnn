from DataSet import DataSet
from DataList import DataList
from DataTable import DataTable

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
    plot_file("new_format/5_assorted.txt")

#-------------------------------------------------------------------------------
# Plot function
#-------------------------------------------------------------------------------

def plot_file(results_name):

    dataList = create_dataList(
        tokenize_file(
            results_name
        )
    )

    dataTable = create_dataTable(dataList)
    print(dataTable.getSize())

    filename = results_name[: -4]
    config = open(filename + "_configs.txt", "w+")
    table_range = range(dataTable.getSize())
    for i in table_range:
        dataList = dataTable.getDataListAt(i)
        '''
        config.write(
            str(i) + " - " +
            "data: " + dataSet.data +
            " | steps: " + dataSet.steps +
            " | filters: " + dataSet.filters +
            " | sizes: " + dataSet.filt_sizes +
            " | dense: " + dataSet.dense +
            " | logits: " + dataSet.logits + "\n"
        )
        '''

        plt.scatter(dataList.getHistory(), dataList.getAverageAccuracy())
    plt.show()

def create_dataTable(dataList):
    dataTable = DataTable(None)
    indices = range(dataList.getSize())

    #TODO: hacky dataList.dList
    for dataSet in dataList.dList:
        if not dataTable.isEmpty():
            print(dataTable.accuracyToString())
        print(dataSet.accuracy)
        if dataTable.isEmpty():
            dataTable = DataTable(dataSet)
        else:
            for i in range(dataTable.size()):
                if dataSet.isSameType(dataSettable.getDataSet(i, 0)):
                    dataTable.getRow().add(dataSet)
                    dataSet = None
            if not dataSet == None:
                dataTable.add(DataList(dataSet))

    return dataTable

def create_dataList(results):
    dataSet = None
    dataList = DataList(None)

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

            dataList.add(dataSet)

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

    return dataList

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
