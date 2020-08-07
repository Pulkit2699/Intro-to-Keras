# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:17:20 2020

@author: pulki
"""

import tensorflow as tf
from tensorflow import keras

def get_dataset(training=True):
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    if training:
        return (train_images, train_labels)
    else:
        return (test_images, test_labels)