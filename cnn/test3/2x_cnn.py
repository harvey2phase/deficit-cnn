from __future__ import absolute_import, division, print_function

import numpy as np
import os
import tensorflow as tf

# 0: all messages are logged (default behavior)
# 1: INFO messages are not printed
# 2: INFO and WARNING messages are not printed
# 3: INFO, WARNING, and ERROR messages are not printed
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

PROJECT_PATH = "/project/def-arutenbe/harveyw/summer-research/"

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

def main():

    data_folder = "cnn_data/e4_age80/cohort1/"
    node = 50
    bias = "unbiased_"

    pool = [2, 2]
    pool_stride = 2
    steps = 2 * 10 ** 5
    dense = 256
    logits = 2

    set_data(data_folder = data_folder, node = node, history = 2, bias = bias)
    set_hype(
        filters = [64],
        filter_sizes = [[5, 5]],
        pool = pool,
        pool_stride = pool_stride,
        steps = steps,
        dense = dense,
        logits = logits
    )
    for _ in range(100):
        run("results/test3/2x.txt")

#-------------------------------------------------------------------------------
# CNN Model
#-------------------------------------------------------------------------------

def deficit_cnn_model(features, labels, mode):

    ''' Input Layer '''
    # Reshape X to 4-D tensor: [batch_size, width, height, channels]
    layer = tf.reshape(features, [-1, NODE, HISTORY, 1])

    length = NODE
    width = HISTORY
    for i in range(CONV_COUNT):

        ''' Convolutional Layer '''
        # Output Tensor Shape: [batch_size, length, width, filter size]
        layer = tf.layers.conv2d(
            inputs = layer,
            filters = CONV_FILTERS[i],
            kernel_size = CONV_SIZES[i],
            padding = "same",
            activation = tf.nn.relu
        )

        ''' Pooling Layer '''
        # Output Tensor Shape: [batch_size, length / 2, width / 2 , filter size]
        layer = tf.layers.max_pooling2d(
            inputs = layer,
            pool_size = POOL_SIZE,
            strides = POOL_STRIDE
        )

        length = int(length / 2)
        width = int(width / 2)

    ''' Flatten tensor into a batch of vectors '''
    pool2_flat = tf.reshape(layer, [-1, CONV_FILTERS[i] * length * width])

    ''' Dense Layer '''
    # TODO update comment
    # Densely connected layer with 1024 neurons
    # Tensor Shape: [batch_size, 1024]
    dense = tf.layers.dense(
        inputs = pool2_flat,
        units = DENSE_UNITS,
        activation = tf.nn.relu
    )

    ''' Add dropout operation '''
    # TODO update comment
    # 0.6 probability that element will be kept
    # Tensor Shape: [batch_size, 1024]
    dropout = tf.layers.dropout(
        inputs = dense,
        rate = DROPOUT_RATE,
        training = mode == tf.estimator.ModeKeys.TRAIN
    )

    ''' Logits layer '''
    # Input Tensor Shape: [batch_size, 1024]
    # Tensor Shape: [batch_size, 1024]
    logits = tf.layers.dense(
        inputs = dropout,
        units = LOGITS_UNITS
    )

    predictions = {
        # Generate predictions (for PREDICT and EVAL mode)
        "classes": tf.argmax(input = logits, axis = 1),

        # Add `softmax_tensor` to the graph.
        # It is used for PREDICT and by the `logging_hook`.
        "probabilities": tf.nn.softmax(logits, name = "softmax_tensor")
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(
            mode = mode,
            predictions = predictions
        )

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(
        labels = labels,
        logits = logits
    )

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:

        optimizer = tf.train.GradientDescentOptimizer(
            learning_rate = LEARNING_RATE
        )
        train_op = optimizer.minimize(
            loss = loss,
            global_step = tf.train.get_global_step()
        )

        return tf.estimator.EstimatorSpec(
            mode = mode,
            loss = loss,
            train_op = train_op
        )

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels = labels,
            predictions = predictions["classes"]
        ),
        "false negatives": tf.metrics.false_negatives(
            labels = labels,
            predictions = predictions["classes"]
        ),
        "false positives": tf.metrics.false_positives(
            labels = labels,
            predictions = predictions["classes"]
        ),
        "true positives": tf.metrics.true_positives(
            labels = labels,
            predictions = predictions["classes"]
        ),
        "true negatives": tf.metrics.true_negatives(
            labels = labels,
            predictions = predictions["classes"]
        )
    }

    return tf.estimator.EstimatorSpec(
        mode = mode,
        loss = loss,
        eval_metric_ops = eval_metric_ops
    )

#-------------------------------------------------------------------------------
# Run Function
#-------------------------------------------------------------------------------

def run(filename):

    ''' Logging '''
    #tensors_to_log = {"probabilities": "softmax_tensor"}
    #logging_hook = tf.train.LoggingTensorHook(
    #    tensors = tensors_to_log,
    #    every_n_iter = 50
    #)

    ''' Data '''
    train_data = np.loadtxt(PROJECT_PATH + TRAIN_SET)
    eval_data = np.loadtxt(PROJECT_PATH + EVAL_SET)

    train_labels = np.loadtxt(
        PROJECT_PATH + TRAIN_LABELS,
        dtype = np.int32
    )

    eval_labels = np.loadtxt(
        PROJECT_PATH + EVAL_LABELS,
        dtype = np.int32
    )

    ''' Classifier'''
    classifier = tf.estimator.Estimator(model_fn = deficit_cnn_model)

    ''' Training '''
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

    ''' Evaluation '''
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x = eval_data,
        y = eval_labels,
        num_epochs = 1,
        shuffle = False
    )
    eval_results = classifier.evaluate(input_fn = eval_input_fn)

    ''' Record results '''
    results = open(PROJECT_PATH + filename, "a+")

    results.write(
        "data: " + DATA_FOLDER + "\t" +
        "history: " + str(HISTORY) + "\t" +
        "nodes: " + str(NODE) + "\n"
    )
    results.write(
        "filters: " + str(CONV_FILTERS) + "\t" +
        "sizes: " + str(CONV_SIZES) + "\n"
    )
    results.write(
        "pool: " + str(POOL_SIZE) + "\t" +
        "stride: " + str(POOL_STRIDE) + "\n"
    )
    results.write(
        "dense: " + str(DENSE_UNITS) + "\t" +
        "logits: " + str(LOGITS_UNITS) + "\n"
    )
    results.write(
        "steps: " + str(STEPS) + "\t" +
        "lr: " + str(LEARNING_RATE) + "\t" +
        "dr: " + str(DROPOUT_RATE) + "\t" +
        "batch: " + str(BATCH_SIZE) + "\n"
    )
    results.write(str(eval_results) + "\n")
    results.write("---\n")

    results.close()

#-------------------------------------------------------------------------------
# CNN parameter tests
#-------------------------------------------------------------------------------

'''
Sample call:
test_2_layer_cnn(
    data_folder = "cnn_data/e4_age80/200_annk/cohort1/",
    history = 4,
    nodes = 200,
    bias = "unbiased_",
    output_filename = "results/200annk/4assorted.txt"
)
'''
def test_2_layer_cnn(data_folder, history, nodes, bias, output_filename):

    filtersez = [
        [32, 64],
        [64, 128],
        [64, 64]
    ]
    sizesez = [
        [[5, 5], [5, 5]],
        [5, 5]
    ]

    pool_size = [2, 2]
    pool_stride = 2

    stepsez = [
        1 * 10 ** 5,
        2 * 10 ** 5,
        5 * 10 ** 4
    ]

    denses = [
        128,
        256,
        512
    ]
    logitsez = [
        2,
        4,
        8
    ]

    for _ in range(100):
        for filters in filtersez:
            for sizes in sizesez:

                for steps in stepsez:

                    for dense in denses:
                        for logits in logitsez:
                            set_data(data_folder, nodes, history, bias)
                            set_hype(
                                filters,
                                sizes,
                                pool_size,
                                pool_stride,
                                steps,
                                dense,
                                logits
                            )
                            run(output_filename)

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

''' Data  '''
HISTORY = None
NODE = None

TRAIN_SET = None
TRAIN_LABELS = None
EVAL_SET = None
EVAL_LABELS = None

''' Hyperparameters '''
CONV_FILTERS = None
CONV_SIZES = None
CONV_COUNT = None

POOL_SIZE = None
POOL_STRIDE = None

DENSE_UNITS = None
LOGITS_UNITS = None

STEPS = None
LEARNING_RATE = 10 ** -4
DROPOUT_RATE = 0.4
BATCH_SIZE = 100

#-------------------------------------------------------------------------------
# Setters for global variables
#-------------------------------------------------------------------------------

def set_data(data_folder, node, history, bias):
    global NODE
    global DATA_FOLDER
    global HISTORY
    global TRAIN_SET
    global TRAIN_LABELS
    global EVAL_SET
    global EVAL_LABELS

    DATA_FOLDER = data_folder
    NODE = node
    HISTORY = history
    history = str(history)

    # Shape: [training_size, NODE * HISTORY]
    TRAIN_SET = DATA_FOLDER + bias + history + "x5y_train_set.txt"
    TRAIN_LABELS = DATA_FOLDER + bias + history + "x5y_train_labels.txt"
    EVAL_SET = DATA_FOLDER + bias + history + "x5y_eval_set.txt"
    EVAL_LABELS = DATA_FOLDER + bias + history + "x5y_eval_labels.txt"

def set_hype(filters, filter_sizes, pool, pool_stride, steps, dense, logits):
    global CONV_FILTERS
    global CONV_SIZES
    global CONV_COUNT
    global POOL_SIZE
    global POOL_STRIDE
    global STEPS
    global DENSE_UNITS
    global LOGITS_UNITS

    CONV_FILTERS = filters
    CONV_SIZES = filter_sizes
    CONV_COUNT = len(CONV_FILTERS)
    POOL_SIZE = pool
    POOL_STRIDE = pool_stride
    STEPS = steps
    DENSE_UNITS = dense
    LOGITS_UNITS = logits

main()
