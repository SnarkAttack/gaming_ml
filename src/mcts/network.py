from tensorflow import keras
from tensorflow.keras import layers


class ConvolutionalBlock(layers.Layer):

    def __init__(self, filters=256, kernel_size=(3, 3), strides=(1, 1)):
        super().__init__()
        self._conv = layers.Conv2D(
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding="same"
        )
        self._batch_norm = layers.BatchNormalization()
        self._relu = layers.ReLU()

    def call(self, inputs):
        x = self._conv(inputs)
        x = self._batch_norm(x)
        x = self._relu(x)

        return x

class ResidualBlock(layers.Layer):

    def __init__(self, filters, kernel_size, strides):
        super().__init__()
        self._conv_block_1 = ConvolutionalBlock(filters, kernel_size, strides)
        self._conv_block_2 = ConvolutionalBlock(filters, kernel_size, strides)
        self._relu = layers.ReLU()

    def call(self, inputs):
        x = self._conv_block_1(inputs)
        x = self._conv_block_2(x)
        x = layers.Add()([inputs, x])
        x = self._relu(x)

        return x

class ValueBlock(layers.Layer):

    def __init__(self, dense1=256):
        super().__init__()
        self._conv = layers.Conv2D(filters=1, kernel_size=(1, 1), strides=(1, 1))
        self._batch_norm = layers.BatchNormalization()
        self._relu_1 = layers.ReLU()
        self._flat = layers.Flatten()
        self._dense_1 = layers.Dense(dense1, activation='relu')
        self._relu_2 = layers.ReLU()
        self._dense_2 = layers.Dense(1, activation='tanh')

    def call(self, inputs):
        x = self._conv(inputs)
        x = self._batch_norm(x)
        x = self._relu_1(x)
        x = self._flat(x)
        x = self._dense_1(x)
        x = self._relu_2(x)
        x = self._dense_2(x)

        return x

class PolicyHeadBlock(layers.Layer):

    def __init__(self, policy_options=1):
        super().__init__()
        self._conv = layers.Conv2D(filters=2, kernel_size=(1,1), strides=(1,1))
        self._batch_norm = layers.BatchNormalization()
        self._relu = layers.ReLU()
        self._flat = layers.Flatten()
        self._dense = layers.Dense(policy_options, activation='softmax')

    def call(self, inputs):
        x = self._conv(inputs)
        x = self._batch_norm(x)
        x = self._relu(x)
        x = self._flat(x)
        x = self._dense(x)

        return x

class Network(keras.Model):

    def __init__(self, filters, kernel_size, strides=(1,1), num_layers=20, value_dense=256, policy_options=1):
        super().__init__()
        self._conv_block = ConvolutionalBlock(filters, kernel_size, strides)
        self._res_blocks = []
        for _ in range(num_layers):
            self._res_blocks.append(ResidualBlock(filters, kernel_size, strides))
        self._value_block = ValueBlock(value_dense)
        self._policy_block = PolicyHeadBlock(policy_options)

    def call(self, inputs):
        x = self._conv_block(inputs)
        for res_block in self._res_blocks:
            x = res_block(x)
        val = self._value_block(x)
        policy = self._policy_block(x)

        return [val, policy]

