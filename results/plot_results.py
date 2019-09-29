from DataConfig import DataConfig
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
<<<<<<< HEAD
    plot_file("test0/all.txt", "save")
=======
    plot_file("test1/all.txt", "show", img_name = "test1")
    #plot_file("test2/all.txt", "save", img_name = "test2")
    #plot_file("test3/all.txt", "save", img_name = "test3")
    #plot_file("test4/all.txt", "save", img_name = "test4")
>>>>>>> 6e495fc9ad90486b5fc3b71ac30fc34242714b15

#-------------------------------------------------------------------------------
# Plot function
#-------------------------------------------------------------------------------

def plot_file(results_name, display_mode, img_name = ""):
    tokenized_list = tokenize_file(results_name)

    results_name = results_name[: -4]
    tokenized_file = open(results_name + "_tokenized.txt", "w+")
    for token in tokenized_list:
        tokenized_file.write(token + "\n")
    tokenized_file.close()

    dataTable = create_dataTable(create_dataList(tokenized_list))

    dataTable.plotWithError(results_name, display_mode, img_name = img_name)
    dataTable.plotROC(results_name, display_mode, img_name = img_name)

    #fig, ax = plt.subplots()

    config = open(results_name  + "_configs.txt", "w+")
    config.write(dataTable.getConfigs())
    config.close()

def create_dataTable(dataList):
    dataTable = DataTable(None)
    indices = range(dataList.getSize())

    histories = []
    counts = []
    for i in indices:
        dataTable.add(dataList.getDataSetAt(i), histories, counts)

    return dataTable

def create_dataList(results):
    dataSet = None
    dataList = DataList(None)

    i = 0
    indices = len(results)
    data, history, steps = None, None, None
    filters, filt_sizes, dense, logits = None, None, None, None
    accuracy = None
    true_positive, false_negative = None, None
    true_negative, false_positive = None, None
    while i < indices:
        if results[i] == "data":
            i += 1
            data = results[i]

        elif results[i] == "history":
            i += 1
            history = int(results[i])

        elif results[i] == "filters":
            i += 1
            filters = [int(results[i])]
            i += 1
            while results[i].isdigit():
                filters.append(int(results[i]))
                i += 1
            i -= 1

        elif results[i] == "sizes":
            i += 1
            filt_sizes = [int(results[i])]
            i += 1
            while results[i].isdigit():
                filt_sizes.append(int(results[i]))
                i += 1
            i -= 1

        elif results[i] == "dense":
            i += 1
            dense = int(results[i])

        elif results[i] == "logits":
            i += 1
            logits = int(results[i])

        elif results[i] == "accuracy":
            i += 1
            accuracy = float(results[i])

        elif results[i] == "false":
            i += 1
            if results[i] == "negatives":
                i += 1
                false_negative = int(float(results[i]))
            elif results[i] == "positives":
                i += 1
                false_positive = int(float(results[i]))

        elif results[i] == "true":
            i += 1
            if results[i] == "positives":
                i += 1
                true_positive = int(float(results[i]))
            elif results[i] == "negatives":
                i += 1
                true_negative = int(float(results[i]))

        elif results[i] == "global_step":
            i += 1
            steps = int(results[i])

        elif results[i] == "---":
            dataList.add(
                DataSet(
                    DataConfig(
                        data,
                        history,
                        steps,
                        filters,
                        filt_sizes,
                        dense,
                        logits
                    ),
                    accuracy,
                    true_positive,
                    false_negative,
                    true_negative,
                    false_positive
                )
            )
            data, history, steps = None, None, None
            filters, filt_sizes, dense, logits = None, None, None, None
            accuracy = None
            true_positive, false_negative = None, None
            true_negative, false_positive = None, None

        i += 1

    return dataList

def tokenize_file(results_name):
    results_file = open(results_name, "r")
    results = []

    for word in results_file.read().split():
        word = word.replace(",", "").replace("[", "").replace("\'", "")
        word = word.replace("]", "").replace("{", "").replace("}", "")
        word = word.replace(":", "").replace("/", "")
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
