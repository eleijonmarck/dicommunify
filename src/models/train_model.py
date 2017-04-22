#!/usr/local/bin python3
#-*- coding: utf-8 -*-

import numpy as np
np.random.seed(13) # reproducability

# Sequential model type from Keras. This is simply a linear stack of neural network layers, and it's perfect for the type of feed-forward CNN
from keras import Sequential

# the "core" layers from Keras. These are the layers that are used in almost any neural network:
from keras.layers import Dense, Dropout, Activation, Flatten

# we'll import the CNN layers from Keras. These are the convolutional layers that will help us efficiently train on image data
from keras.layers import Convolution2D, MaxPooling2D

# This will help us transform our data 
from keras.utils import np_utils


#####################
# Train from our dataset
#####################

## TODO: create dicommunify.dataset class with method xray
from dicommunify.dataset import xray

x, y = xray.load_data()
