from DataSet import DataSet
from DataList import DataList

import sys

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

    def accuracyToString(self):
        string = ""
        for dataList in self.dTable:
            string += dataList.accuracyToString() + "\n"
        return string

    def isEmpty(self):
        if not self.dTable:
            return True
        elif self.dTable[0].isEmpty():
            #print(self.dTable[0].accuracyToString())
            #print("Table is empty")
            return True
        return False

    def getSize(self):
        return len(self.dTable)

    def add(self, dataSet: DataSet):
        if self.isEmpty():
            #print(self.dTable)
            self.dTable.append(DataList(dataSet))
            #print(self.dTable)
        else:
            for dataList in self.dTable:
                if dataList.getFirst().isSameType(DataSet):
                    dataList.add(para)
                    return
            self.dTable.append(DataList(param))

    def getDataListAt(self, row):
        return self.dTable[row]

    def getDataSet(self, row, index):
        return self.dTable[row][index]
