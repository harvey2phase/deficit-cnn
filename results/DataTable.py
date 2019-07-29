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
    # Plot functions
    #---------------------------------------------------------------------------

    def plotCountWithConfigName(self, ax, results_name, display_mode):
        for dataList in self.dTable:
            if dataList.getSize() < 2:
                c = 'r'
            elif dataList.getSize() < 6:
                c = 'g'
            elif dataList.getSize() < 11:
                c = 'b'
            else:
                c = 'k'

            dataList.scatterPlot(ax, colour = c, anno = dataList.name)
        if display_mode == "show":
            plt.show()
        else:
            plt.savefig(results_name + "_count.png", dpi = 400)
        plt.clf()

    def plotFilters(self, ax, results_name, display_mode):
        for dataList in self.dTable:
            filters = str(dataList.getFirst().dataConfig.filters)
            label = ""
            if (
                filters == "[16, 64, 64, 128]"
                or filters == "[32, 64, 128]"
                or filters == "[64, 128]"
                or filters == "[128]"
            ):
                c = "b"
            elif (
                filters == "[16, 32, 64, 128]"
                or filters == "[32, 64, 64]"
                or filters == "[64, 64]"
                or filters == "[64]"
            ):
                c = "g"
            elif (
                filters == "[16, 32, 64]"
                or filters == "[32, 64]"
                or filters == "[32]"
            ):
                c = "r"
            else:
                c = "k"
                label = filters
            dataList.scatterPlot(ax, colour = c, label = label)
        if display_mode == "show":
            plt.show()
        else:
            plt.savefig(results_name + "_filters.png", dpi = 400)
        plt.clf()

    def plotSteps(self, ax, results_name, display_mode):
        for dataList in self.dTable:
            steps = str(dataList.getFirst().dataConfig.steps)
            label = ""
            if steps == "200000":
                c = "b"
            elif steps == "100000":
                c = "g"
            elif steps == "50000":
                c = "r"
            else:
                c = "k"
                label = steps
            dataList.scatterPlot(ax, colour = c, label = label)
        if display_mode == "show":
            plt.show()
        else:
            plt.savefig(results_name + "_steps.png", dpi = 400)
        plt.clf()

    def plotSizes(self, ax, results_name, display_mode):
        for dataList in self.dTable:
            sizes = str(dataList.getFirst().dataConfig.filt_sizes)
            anno = ""
            if sizes == "[5, 5]":
                c = "b"
            elif sizes == "[5, 5, 5, 5, 5, 5, 5, 5]":
                c = "g"
            elif sizes == "[5, 5, 5, 5, 5, 5]":
                c = "m"
            elif sizes == "[5, 5, 5, 5]":
                c = "r"
            elif sizes == "[5, 5, 5]":
                c = "y"
            else:
                c = "k"
                anno = sizes
            dataList.scatterPlot(ax, colour = c, anno = anno)
        if display_mode == "show":
            plt.show()
        else:
            plt.savefig(results_name + "_sizes.png", dpi = 400)
        plt.clf()

    def plotDense(self, ax, results_name, display_mode):
        plt.title("b - 512, g - 256, r - 128")
        for dataList in self.dTable:
            dense = str(dataList.getFirst().dataConfig.dense)
            anno = ""
            if dense == "512":
                c = "b"
            elif dense == "256":
                c = "g"
            elif dense == "128":
                c = "r"
            else:
                c = "k"
                anno = dense
            dataList.scatterPlot(ax, colour = c, anno = anno)
        if display_mode == "show":
            plt.show()
        else:
            plt.savefig(results_name + "_dense.png", dpi = 400)
        plt.clf()

    def plotLogits(self, ax, results_name, display_mode):
        plt.title("b - 2, g - 4, r - 8")
        for dataList in self.dTable:
            logits = str(dataList.getFirst().dataConfig.logits)
            anno = ""
            if logits == "2":
                c = "b"
            elif logits == "4":
                c = "g"
            elif logits == "8":
                c = "r"
            else:
                c = "k"
                anno = logits
            dataList.scatterPlot(ax, colour = c, anno = anno)
        if display_mode == "show":
            plt.show()
        else:
            plt.savefig(results_name + "_logits.png", dpi = 400)
        plt.clf()

    #---------------------------------------------------------------------------
    # Extended functions
    #---------------------------------------------------------------------------

    def getConfigs(self):
        configs = ""
        for dataList in self.dTable:
            configs += dataList.name + "\n"
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

