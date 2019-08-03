from DataSet import DataSet

import sys
import numpy as np
import matplotlib.pyplot as plt

class DataList:

    def __init__(self, param):
        if param == None:
            self.dList = []
        elif isinstance(param, DataSet):
            self.dList = [param]
        else:
            sys.exit("DataList init error")
        self.name = "default"

    def add(self, dataSet: DataSet):
        self.dList.append(dataSet)


    #---------------------------------------------------------------------------
    # Stats calculation
    #---------------------------------------------------------------------------

    def getStdDevAccuracy(self):
        mean = self.getAverageAccuracy()
        diff_squared_sum = 0
        for dataSet in self.dList:
            diff_squared_sum += (dataSet.accuracy - mean) ** 2
        return np.sqrt(diff_squared_sum / (self.getSize() - 1))

    def getAverageAccuracy(self):
        totalAccuracy = 0
        for dataSet in self.dList:
            totalAccuracy += dataSet.accuracy
        return totalAccuracy / len(self.dList)

    #---------------------------------------------------------------------------
    # Plots
    #---------------------------------------------------------------------------

    def scatterWithError(self, x_list, y_list):
        std_dev = self.getStdDevAccuracy()
        history = self.getHistory()
        accuracy = self.getAverageAccuracy()

        x_list.append(history)
        y_list.append(accuracy)

        plt.scatter(history, accuracy, c = "k")
        if history == 2:
            dev_label = "standard deviation"
            err_label = "standard eror of the mean"
        else:
            dev_label = ""
            err_label = ""

        plt.errorbar(
            history,
            accuracy,
            yerr = std_dev,
            ecolor = "r",
            capsize = 8,
            label = dev_label
        )
        plt.errorbar(
            history,
            accuracy,
            yerr = std_dev / np.sqrt(self.getSize()),
            ecolor = "b",
            capsize = 5,
            label = err_label
        )

    def scatterPlot(self, ax, colour, anno = ""):
        his, acc = self.getHistory(), self.getAverageAccuracy()
        ax.scatter(his, acc, c = colour)
        ax.annotate(anno, (his, acc))


    #---------------------------------------------------------------------------
    # Checks
    #---------------------------------------------------------------------------

    def isEmpty(self):
        if self.dList:
            return False
        return True

    #---------------------------------------------------------------------------
    # Get methods
    #---------------------------------------------------------------------------

    def getFirst(self):
        return self.dList[0]

    def getHistory(self):
        return self.getFirst().dataConfig.history

    def getDataSetAt(self, i):
        return self.dList[i]

    def getSize(self):
        return len(self.dList)

    #---------------------------------------------------------------------------
    # toString method
    #---------------------------------------------------------------------------

    def accuracyToString(self):
        string = ""
        for dataSet in self.dList:
            string += str(dataSet.accuracy) + ", "
        return string[: -2]

    def configToString(self):
        configs = self.name + "\n"
        for dataSet in self.dList:
            configs += dataSet.dataConfig.toString() + "\n"
        return configs + "\n"

