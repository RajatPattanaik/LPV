# -*- coding: utf-8 -*-
"""DL_3_fashionClothing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dOsH2zcOdk8xCHFmXm1eEhgNC3Ezaxu6
"""

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

plt.imshow(x_train[1])

plt.imshow(x_train[0])

# Next, we will preprocess the data by scaling the pixel values to be between 0 and 1, and then reshaping the images to be 28x28 pixels.
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

model = keras.Sequential([
keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
# 32 filters (default), randomly initialized
# 3*3 is Size of Filter
# 28,28,1 size of Input Image
# No zero-padding: every output 2 pixels less in every dimension
# in Paramter shwon 320 is value of weights: (3x3 filter weights + 32 bias) * 32 filters
# 32*3*3=288(Total)+32(bias)= 320
keras.layers.MaxPooling2D((2,2)),
# It shown 13 * 13 size image with 32 channel or filter or depth.
keras.layers.Dropout(0.25),
# Reduce Overfitting of Training sample drop out 25% Neuron
keras.layers.Conv2D(64, (3,3), activation='relu'),
# Deeper layers use 64 filters
# 3*3 is Size of Filter
# Observe how the input image on 28x28x1 is transformed to a 3x3x64 feature map
# 13(Size)-3(Filter Size )+1(bias)=11 Size for Width and Height with 64 Depth or filtter or channel
# in Paramter shwon 18496 is value of weights: (3x3 filter weights + 64 bias) * 64 filters
# 64*3*3=576+1=577*32 + 32(bias)=18496
keras.layers.MaxPooling2D((2,2)),
# It shown 5 * 5 size image with 64 channel or filter or depth.
keras.layers.Dropout(0.25),

keras.layers.Conv2D(128, (3,3), activation='relu'),
# Deeper layers use 128 filters
# 3*3 is Size of Filter
# Observe how the input image on 28x28x1 is transformed to a 3x3x128 feature map
# It show 5(Size)-3(Filter Size )+1(bias)=3 Size for Width and Height with 64 Depth or filtter or channel
# 128*3*3=1152+1=1153*64 + 64(bias)= 73856
# To classify the images, we still need a Dense and Softmax layer.
# We need to flatten the 3x3x128 feature map to a vector of size 1152
keras.layers.Flatten(),
keras.layers.Dense(128, activation='relu'),
# 128 Size of Node in Dense Layer
# 1152*128 = 147584
keras.layers.Dropout(0.25),
keras.layers.Dense(10, activation='softmax')
# 10 Size of Node another Dense Layer
# 128*10+10 bias= 1290
])
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)