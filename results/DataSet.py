
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

    def equals(self, dataSet):
        if (
            self.data == dataSet.data
            or self.history == dataSet.history
            or self.steps == dataSet.steps
            or self.filters == dataSet.filters
            or self.filt_sizes == dataSet.filt_sizes
            or self.dense == dataSet.dense
            or self.logits == dataSet.logits
        ):
            return False
        return True
