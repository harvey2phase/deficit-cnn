from __future__ import absolute_import, division, print_function

import numpy as np
import tensorflow as tf

from cnn_model import deficit_cnn_model

#-------------------------------------------------------------------------------
# Data paths and constants
#-------------------------------------------------------------------------------

def set_data(history, node_count):

    global HISTORY
    global NODE_COUNT
    global TRAIN_SET
    global TRAIN_LABELS
    global EVAL_SET
    global EVAL_LABELS

    HISTORY = history
    NODE_COUNT = node_count

    # Shape: [training_size, NODE_COUNT * HISTORY]
    TRAIN_SET = str(HISTORY) + "x5y_train_set.txt"
    TRAIN_LABELS = str(HISTORY) + "x5y_train_labels.txt"
    EVAL_SET = str(HISTORY) + "x5y_eval_set.txt"
    EVAL_LABELS = str(HISTORY) + "x5y_eval_labels.txt"

#-------------------------------------------------------------------------------
# Hyperparameters
#-------------------------------------------------------------------------------

def set_hype(filters, sizes):
    global CONV_FILTERS
    global CONV_SIZES
    global CONV_COUNT

    CONV_FILTERS = [32, 64, 128]
    CONV_SIZES = [[5, 5], [5, 5], [5, 5]]

    CONV_COUNT = len(CONV_FILTERS)


#-------------------------------------------------------------------------------
# Load data and setup logging
#-------------------------------------------------------------------------------

train_data = np.loadtxt(PATH + TRAIN_SET)
eval_data = np.loadtxt(PATH + EVAL_SET)

train_labels = np.loadtxt(
    PATH + TRAIN_LABELS,
    dtype = np.int32
)
eval_labels = np.loadtxt(
    PATH + EVAL_LABELS,
    dtype = np.int32
)

tensors_to_log = {"probabilities": "softmax_tensor"}
logging_hook = tf.train.LoggingTensorHook(
    tensors = tensors_to_log,
    every_n_iter = 50
)


#-------------------------------------------------------------------------------
# Create classifier, train, and evaluate
#-------------------------------------------------------------------------------

classifier = tf.estimator.Estimator(model_fn = deficit_cnn_model)

train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x = {'x': train_data},
    y = train_labels,
    batch_size = BATCH_SIZE,
    num_epochs = None,
    shuffle = True
)

classifier.train(
    input_fn = train_input_fn,
    steps = STEPS,
    hooks = [logging_hook]
)

'''
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    x = eval_data,
    y = eval_labels,
    num_epochs = 1,
    shuffle = False
)
eval_results = classifier.evaluate(input_fn = eval_input_fn)
print(eval_results)

'''
print("DONE")
