from DataSet import DataSet
from DataList import DataList

import sys
import matplotlib.pyplot as plt

class DataTable:

    def __init__(self, param):
        if param == None:
            self.dTable = []
        elif isinstance(param, DataSet):
            self.dTable = [DataList(param)]
        else:
            sys.exit("DataList init error")

    def add(self, dataSet: DataSet, histories, counts):
        if self.isEmpty():
            self.addDataList(dataSet, histories, counts)
        else:
            # TODO
            for dataList in self.dTable:
                history = dataList.getHistory()
                if not history in histories:
                    histories.append(history)
                    counts.append(1)
                else:
                    counts[histories.index(history)] += 1
                dataSet.dataConfig.name = (
                    str(history) + "." +
                    str(counts[histories.index(history)])
                )
                if dataList.getFirst().isSameConfig(dataSet.dataConfig):
                    dataList.add(dataSet)
                    return
            self.dTable.append(DataList(dataSet))

    def addDataList(self, dataSet, histories, counts):
        histories.append(dataSet.dataConfig.history)
        counts.append(1)
        dataSet.dataConfig.name = str(dataSet.dataConfig.history) + ".1"
        self.dTable.append(DataList(dataSet))

    #---------------------------------------------------------------------------
    # Extended functions
    #---------------------------------------------------------------------------

    def scatterPlot(self, ax, results_name):
        for dataList in self.dTable:
            dataList.scatterPlot(ax)
        plt.savefig(results_name + ".png", dpi = 400)

    def getConfigs(self):
        configs = ""
        for dataList in self.dTable:
            configs += (dataList.configToString() + "\n")
        return configs

    #---------------------------------------------------------------------------
    # Checks
    #---------------------------------------------------------------------------

    def isEmpty(self):
        if not self.dTable:
            return True
        elif self.dTable[0].isEmpty():
            return True
        return False

    #---------------------------------------------------------------------------
    # Get methods
    #---------------------------------------------------------------------------

    def getSize(self):
        return len(self.dTable)

    def getCount(self):
        if self.isEmpty():
            return 0
        count = 0
        for dataList in self.dTable:
            count += dataList.getSize()
        return count

    def getDataListAt(self, row):
        return self.dTable[row]

    def getDataSet(self, row, index):
        return self.dTable[row][index]

    #---------------------------------------------------------------------------
    # toString method
    #---------------------------------------------------------------------------

    def accuracyToString(self):
        string = ""
        for dataList in self.dTable:
            string += dataList.accuracyToString() + "\n"
        return string

