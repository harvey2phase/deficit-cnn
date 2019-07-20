from DataSet import DataSet
from DataList import DataList

import sys
import matplotlib.pyplot as plt

class DataTable:

    def __init__(self, param):
        if param == None:
            self.dTable = []
            #print(self.dTable[0].dList)
            #if self.dTable[0].dList == []:
            #    print("empty!")
            #if self.dTable[0].isEmpty():
            #    print("empty!")
        elif isinstance(param, DataList):
            self.dTable = [param]
        elif isinstance(param, DataSet):
            self.dTable = [DataList(param)]
        else:
            sys.exit("DataList init error")

    def add(self, dataSet: DataSet):
        if self.isEmpty():
            self.dTable.append(DataList(dataSet))
        else:
            for dataList in self.dTable:
                if dataList.getFirst().isSameConfig(dataSet.dataConfig):
                    dataList.add(dataSet)
                    return
            self.dTable.append(DataList(dataSet))

    #---------------------------------------------------------------------------
    # Extended functions
    #---------------------------------------------------------------------------

    def scatterPlot(self):
        for dataList in self.dTable:
            dataList.scatterPlot()
        plt.show()

    #---------------------------------------------------------------------------
    # Checks
    #---------------------------------------------------------------------------

    def isEmpty(self):
        if not self.dTable:
            return True
        elif self.dTable[0].isEmpty():
            #print(self.dTable[0].accuracyToString())
            #print("Table is empty")
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

