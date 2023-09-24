import numpy as np
from enum import Enum

from typing import List, Tuple


class ActivationFunction(Enum):
    RELU = lambda x: np.maximum(0, x)
    TANH = lambda x: np.tanh(x)
    LOGISTIC = lambda x: 1 / (1 + np.exp(-x))


class MLP:
    input_size = 5
    layer_schemas = []
    layers = []

    def __init__(self, input_size: int, layer_schemas: List[Tuple[int, str]]):
        self.input_size = input_size
        self.layer_schemas = layer_schemas

    def initLayers(self) -> None:
        self.layers = []
        self.layers.append(np.random.rand(self.layer_schemas[0][1], self.input_size))

        prev_layer_size = self.layer_schemas[0][1]

        for layer in self.layer_schemas[1:]:
            self.layers.append(np.random.rand(layer[1], prev_layer_size))
            prev_layer_size = layer[1]

        print("These are the layers: " + str(self.layers))

    def forwardPass(self, input_vec: np.ndarray) -> np.ndarray:
        currVal = input_vec
        print("curr_val start is: " + str(currVal))
        for layerIdx in range(len(self.layers)):
            currActivationFunc = self.layer_schemas[layerIdx][0]
            currActivation = np.dot(self.layers[layerIdx], currVal)
            print("curr_val before activation func is: " + str(currActivation))
            currVal = currActivationFunc(currActivation)
            print("curr_val after activation func is: " + str(currVal))
        print("Final curr_val is: " + str(currVal))
        return currVal


if __name__ == '__main__':
    print("Begin construct basic MLP")
    layerSchemas = [(ActivationFunction.LOGISTIC, 5), (ActivationFunction.TANH, 5),
                    (ActivationFunction.TANH, 5), (ActivationFunction.RELU, 5)]
    basicMLP = MLP(5, layerSchemas)
    basicMLP.initLayers()
    basicMLP.forwardPass(np.array([1, 2, 3, 4, 5]))
