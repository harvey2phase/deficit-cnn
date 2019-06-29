from __future__ import absolute_import, division, print_function

import numpy as np
import tensorflow as tf

def deficit_cnn_model(features, labels, mode):

    ''' Input Layer '''
    # Reshape X to 4-D tensor: [batch_size, width, height, channels]
    layer = tf.reshape(features, [-1, NODE_COUNT, HISTORY, 1])
    
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