from DataSet import DataSet


class DataList:
    def __init__(self, param):
        if param == None:
            self.dList = []
        elif isinstance(param, DataSet):
            self.dList = [param]
        else:
            sys.exit("DataList init error")

    def add(self, dataSet: DataSet):
        self.dList.append(dataSet)

    def accuracyToString(self):
        string = ""
        for dataSet in self.dList:
            string += str(dataSet.accuracy) + ", "
        return string[: -2]

    def getFirst():
        return dList[0]

