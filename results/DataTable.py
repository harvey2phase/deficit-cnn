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
            history = dataSet.dataConfig.history
        else:
            for dataList in self.dTable:
                if dataList.getFirst().isSameConfig(dataSet.dataConfig):
                    dataList.add(dataSet)
                    return
            history = dataList.getHistory()
        self.addDataList(dataSet, history, histories, counts)

    def addDataList(self, dataSet, history, histories, counts):
        if not history in histories:
            histories.append(dataSet.dataConfig.history)
            counts.append(1)

            dataList = DataList(dataSet)
            dataList.name = str(dataSet.dataConfig.history) + ".1"

        else:
            counts[histories.index(history)] += 1
            dataList = DataList(dataSet)
            dataList.name = (
                str(history) + "." +
                str(counts[histories.index(history)])
            )

        self.dTable.append(dataList)

    #---------------------------------------------------------------------------
    # Extended functions
    #---------------------------------------------------------------------------

    def scatterPlot(self, ax, results_name):
        #count = 0
        #skip = 3
        #investigate = ["2.82", "4.75"]
        for dataList in self.dTable:
            #if dataList.name in investigate:
            dataList.scatterPlot(ax)
            #count += 1
        plt.show()
        #plt.savefig(results_name + ".png", dpi = 400)

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

