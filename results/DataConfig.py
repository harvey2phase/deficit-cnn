
class DataConfig:

    def __init__(
        self,
        data,
        history,
        steps,
        filters,
        filt_sizes,
        dense,
        logits
    ):
        self.data = data
        self.history = history
        self.steps = steps
        self.filters = filters
        self.filt_sizes = filt_sizes
        self.dense = dense
        self.logits = logits

    #---------------------------------------------------------------------------
    # Checks
    #---------------------------------------------------------------------------

    def isEqual(self, dataConfig):
        if (
            self.data == dataConfig.data
            and self.history == dataConfig.history
            and self.steps == dataConfig.steps
            and self.filters == dataConfig.filters
            and self.filt_sizes == dataConfig.filt_sizes
            and self.dense == dataConfig.dense
            and self.logits == dataConfig.logits
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

    #---------------------------------------------------------------------------
    # toStrnig Method
    #---------------------------------------------------------------------------

    def toString(self):
        return (
            str(self.history) +
            " | " + str(self.steps) +
            " | " + str(self.filters) +
            " | " + str(self.filt_sizes) +
            " | " + str(self.dense) +
            " | " + str(self.logits)
        )
