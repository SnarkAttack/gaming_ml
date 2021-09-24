import numpy as np
from src.mcts.network import ConvolutionalBlock, RedisualBlock

def test_convolutional_block():
    conv_block = ConvolutionalBlock(
        filters=128,
        kernel_size=(2, 2)
    )

    board = np.stack([
        [
            [1, 2, 3],
            [3, 4, 5],
            [4, 5, 6]
        ],
        [
            [5, 6, 7],
            [7, 8, 9],
            [8, 9, 0]
        ]
    ], axis=2).astype(np.float)

    assert board.shape == (3, 3, 2)

    a = np.array([board])

    x = conv_block(a)

    assert x.shape == (1, 2, 2, 128)

