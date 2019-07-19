from DataSet import DataSet
from DataList import DataList

class DataTable:

    def __init__(self, param):
        if param == None:
            self.dTable = [DataList()]
        elif isinstance(param, DataList):
            self.dTable = [param]
        elif isinstance(param, DataSet):
            self.dTable = [DataList(param)]
        else:
            sys.exit("DataList init error")

    def accuracyToString(self):
        string = ""
        for dataList in self.dTable:
            string += dataList.accuracyToString + "\n"
        return string

    def isEmpty(self):
        if self.dTable[0].isEmpty:
            return True
        return False

    def size(self):
        return len(self.dTable)

    def add(self, dataSet: DataSet):
        if self.isEmpty():
            dTable.append(DataList(dataSet))
        else:
            for dataList in dTable:
                if dataList.getFirst().isSameType(param):
                    dataList.add(para)
                    return
            dTable.append(DataList(param))

    def add(self, dataList: DataList):
        self.dTable.append(dataList)

    def getRow(self, row):
        return self.dTable[row]

    def getDataSet(self, row, index):
        return self.dTable[row][index]
