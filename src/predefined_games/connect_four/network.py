from tensorflow import keras
from tensorflow.keras import layers

class Network(keras.Model):

    def __init__(self):
        super().__init__()

        self.input = layers.Input(6, 7, 2)