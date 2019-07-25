from DataSet import DataSet

import sys
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
    # Checks
    #---------------------------------------------------------------------------

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

    def getAverageAccuracy(self):
        totalAccuracy = 0
        for dataSet in self.dList:
            totalAccuracy += dataSet.accuracy
        return totalAccuracy / len(self.dList)

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

