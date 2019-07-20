import sys

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
        if not self.isNotNone:
            sys.exit("DataSet init error. None input detected.")

    #---------------------------------------------------------------------------
    # Checks
    #---------------------------------------------------------------------------

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

    def isNotNone(self):
        if not self.data == None:
            print("d")
            return False
        if not self.history == None:
            print("h")
            return False
        if not self.steps == None:
            print("s")
            return False
        if not self.filters == None:
            print("f")
            return False
        if not self.filt_sizes == None:
            print("fs")
            return False
        if not self.dense == None:
            print("dense")
            return False
        if not self.logits == None:
            print("l")
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
