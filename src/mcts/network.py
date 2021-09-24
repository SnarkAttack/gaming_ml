from tensorflow import keras
from tensorflow.keras import layers


class ConvolutionalBlock(layers.Layer):

    def __init__(self, filters=256, kernel_size=(3, 3), strides=(1, 1)):
        super().__init__()
        self._conv = layers.Conv2D(
            filters=filters,
            kernel_size=kernel_size,
            strides=strides
        )
        self._batch_norm = layers.BatchNormalization()
        self._relu = layers.ReLU()

    def call(self, inputs):
        x = self._conv(inputs)
        x = self._batch_norm(x)
        x = self._relu(x)

        return x

class RedisualBlock(layers.Layer):

    def __init__(self):
        super().__init__()