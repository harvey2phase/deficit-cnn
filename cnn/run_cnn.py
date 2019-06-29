from __future__ import absolute_import, division, print_function

import numpy as np
import tensorflow as tf

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

HISTORY = None
TRAIN_SET = None
TRAIN_LABELS = None
EVAL_SET = None
EVAL_LABELS = None

NODE_COUNT = 50
PATH = "data_sets/e4/tests_age_80/prob_of_death_at_80/"

CONV_FILTERS = None
CONV_SIZES = None
CONV_COUNT = None

POOL_SIZE = [2, 2]
POOL_STRIDE = 2

STEPS = 1 * 10 ** 5
LEARNING_RATE = 10 ** -4
DROPOUT_RATE = 0.4
BATCH_SIZE = 10
LOGITS_UNITS = 10
DENSE_UNITS = 1024

#-------------------------------------------------------------------------------
# Model
#-------------------------------------------------------------------------------

def deficit_cnn_model(features, labels, mode):

    ''' Input Layer '''
    # Reshape X to 4-D tensor: [batch_size, width, height, channels]
    layer = tf.reshape(features['x'], [-1, NODE_COUNT, HISTORY, 1])

    # Image length and width
    length = NODE_COUNT
    width = HISTORY
    for i in range(CONV_COUNT):

        ''' Convolutional Layer '''
        # Computes 32 features using a 5x5 filter with ReLU activation.
        #   Padding is added to preserve width and height.
        # Output Tensor Shape: [batch_size, length, width, filter size]
        layer = tf.layers.conv2d(
            inputs = layer,
            filters = CONV_FILTERS[i],
            kernel_size = CONV_SIZES[i],
            padding = "same",
            activation = tf.nn.relu
        )

        ''' Pooling Layer '''
        # Max pooling layer with a 2x2 filter and stride of 2
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
    # Densely connected layer with 1024 neurons
    # Tensor Shape: [batch_size, 1024]
    dense = tf.layers.dense(
        inputs = pool2_flat,
        units = DENSE_UNITS,
        activation = tf.nn.relu
    )

    ''' Add dropout operation '''
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
        )
    }

    return tf.estimator.EstimatorSpec(
        mode = mode,
        loss = loss,
        eval_metric_ops = eval_metric_ops
    )

#-------------------------------------------------------------------------------
# Setp global variables functions
#-------------------------------------------------------------------------------

def set_data(history):
    global HISTORY
    global TRAIN_SET
    global TRAIN_LABELS
    global EVAL_SET
    global EVAL_LABELS

    HISTORY = history
    history = str(history)

    # Shape: [training_size, NODE_COUNT * HISTORY]
    TRAIN_SET = history + "x5y_train_set.txt"
    TRAIN_LABELS = history + "x5y_train_labels.txt"
    EVAL_SET = history + "x5y_eval_set.txt"
    EVAL_LABELS = history + "x5y_eval_labels.txt"

def set_hype(filters, sizes):
    global CONV_FILTERS
    global CONV_SIZES
    global CONV_COUNT

    CONV_FILTERS = [32, 64, 128]
    CONV_SIZES = [[5, 5], [5, 5], [5, 5]]

    CONV_COUNT = len(CONV_FILTERS)

#-------------------------------------------------------------------------------
# Setup global variables
#-------------------------------------------------------------------------------

set_data(15)
set_hype([32, 64, 128], [[5, 5], [5, 5], [5, 5]])

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

eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    x = eval_data,
    y = eval_labels,
    num_epochs = 1,
    shuffle = False
)
eval_results = classifier.evaluate(input_fn = eval_input_fn)
print(eval_results)
