from __future__ import absolute_import, division, print_function

import numpy as np
import os
import tensorflow as tf

from cnn_model import deficit_cnn_model

#-------------------------------------------------------------------------------
# Data paths and constants
#-------------------------------------------------------------------------------

PATH = "data_sets/e4/tests_age_80/prob_of_death_at_80/"

# Shape: [training_size, 50 * HISTORY]
HISTORY = 15
NODE_COUNT = 50

TRAIN_SET = str(HISTORY) + "x5y_train_set.txt"
TRAIN_LABELS = str(HISTORY) + "x5y_train_labels.txt"
EVAL_SET = str(HISTORY) + "x5y_eval_set.txt"
EVAL_LABELS = str(HISTORY) + "x5y_eval_labels.txt"

#-------------------------------------------------------------------------------
# Hyperparameters
#-------------------------------------------------------------------------------

STEPS = 1 * 10 ** 5
LEARNING_RATE = 10 ** -4
DROPOUT_RATE = 0.4
BATCH_SIZE = 10

CONV_FILTERS = [32, 64, 128]
CONV_SIZES = [[5, 5], [5, 5], [5, 5]]

CONV_COUNT = len(CONV_FILTERS)

POOL_SIZE = [2, 2]
POOL_STRIDE = 2

DENSE_UNITS = 1024
LOGITS_UNITS = 10

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
    x = train_data,
    y = train_labels,
    batch_size = BATCH_SIZE,
    num_epochs = None,
    shuffle = True
)

classifier.train(
    input_fn = train_input_fn,
    steps = STEPS,
    #hooks = [logging_hook]
)

eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    x = eval_data,
    y = eval_labels,
    num_epochs = 1,
    shuffle = False
)
eval_results = classifier.evaluate(input_fn = eval_input_fn)
print(eval_results)
