import sys

class DataSet:

    def __init__(
        self,
        dataConfig,
        accuracy,
        true_positive,
        false_negative,
        true_negative,
        false_positive
    ):
        self.dataConfig = dataConfig
        self.accuracy = accuracy
        self.true_positive = true_positive
        self.false_negative = false_negative
        self.true_negative = true_negative
        self.false_positiv = false_positive
        if not self.isNotNone:
            sys.exit("DataSet init error. None input detected.")

    #---------------------------------------------------------------------------
    # Checks
    #---------------------------------------------------------------------------

    def isSameConfig(self, dataConfig):
        return self.dataConfig.isEqual(dataConfig)

    def isNotNone(self):
        if not self.dataConfig.isNotNone():
            return False
        if not self.accuracy == None:
            print("a")
            return False
        if not self.true_positive == None:
            print("tp")
            return False
        if not self.false_negative == None:
            print("fn")
            return False
        if not self.true_negative == None:
            print("tn")
            return False
        if not self.false_positiv == None:
            print("fp")
            return False
        return True
