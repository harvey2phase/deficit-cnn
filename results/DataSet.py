
class DataSet:

    def __init__(
        self,
        data,
        history,
        steps,
        filters,
        filt_sizes,
        dense,
        logits,
        accuracy,
        true_positive,
        false_negative,
        true_negative,
        false_positive
    ):
        self.data = data
        self.history = history
        self.steps = steps
        self.filters = filters
        self.filt_sizes = filt_sizes
        self.dense = dense
        self.logits = logits
        self.accuracy = accuracy
        self.true_positive = true_positive
        self.false_negative = false_negative
        self.true_negative = true_negative
        self.false_positiv = false_positive

    def __init__(self, data):
        self.data = data

    def isSameType(self, dataSet):
        if (
            self.data == dataSet.data
            and self.history == dataSet.history
            and self.steps == dataSet.steps
            and self.filters == dataSet.filters
            and self.filt_sizes == dataSet.filt_sizes
            and self.dense == dataSet.dense
            and self.logits == dataSet.logits
        ):
            return True
        return False

class DataList:

    dList = []

    def __init__(self, param):
        if param == None:
            pass
        elif isinstance(param, DataSet):
            dList = [param]
        else:
            sys.exit("DataList init error")

    def add(self, dataSet: DataSet):
        self.dList.append(dataSet)

    def accuracyToString(self):
        string = ""
        for dataSet in self.dList:
            string += str(dataSet.accuracy) + ", "
        return string[: -2]

class DataTable:

    def __init__(self, param):
        if isinstance(param, DataList):
            dTable = [param]
        elif isinstance(param, DataSet):
            dTable = [[param]]
        else:
            sys.exit("DataList init error")

    def accuracyToString(self):
        string = ""
        for dataList in dTable:
            string += dataList.accuracyToString + "\n"
        return string

    def size(self):
        return len(dTable)

    def add(self, dataList: DataList):
        dTable.append(dataList)

    def getRow(self, row):
        return dTable[row]

    def getDataSet(self, row, index):
        return dTable[row][index]
