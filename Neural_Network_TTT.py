# Praise Tensorflow
import tensorflow as tf
from tensorflow.keras import layers

# Useful DSS Libraries
import pandas as pd 
import numpy as np 
import seaborn as sns

# S A H A I
import scipy as sp 

# Data8 Stuff (I have no idea what this does tbh)
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)

# Import the game
from game import *

model = tf.keras.Sequential()
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense10, activation = 'softmax')
layers.Dense(64, activation = tf.sigmoid)
layers.Dense(64, kernel_regularizer=tf.keras.regularizers.l1(0.01))
layers.Dense(64, bias_regularizer = tf.keras.regularizers.l2(0.01))
layers.Dense(64, kernel_initializer='orthogonal')
layers.Dense(64, bias_initializer=tf.keras.initializers.constant(2.0))