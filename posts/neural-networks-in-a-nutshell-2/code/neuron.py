# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to show how to define and use a general model of a neuron.
"""


from math import exp, tanh


def unit_step(x):
    if x >= 0:
        return 1
    else:
        return 0

def signal(x):
    if x >= 0:
        return 1
    else:
        return -1

def logsig(x):
    return (1 / (1 + exp(-x)))

tansig = tanh


class Neuron(object):

    def __init__(self, weights, bias, activation=unit_step):
        self.weights = weights
        self.bias = bias
        self.activation = activation

    def fire(self, inputs):
        summed = sum([i*w for (i,w) in zip(inputs, self.weights)])
        return self.activation(summed + self.bias)


if __name__ == '__main__':
    neuron_1 = Neuron([0.4, 0.6, 0.9], -0.8)
    neuron_2 = Neuron([0.4, 0.6, 0.9], -1.5, signal)
    neuron_3 = Neuron([0.4, 0.6, 0.9], -0.8, logsig)
    neuron_4 = Neuron([0.4, 0.6, 0.9], -0.8, tansig)

    inputs = [1, 0, 1]

    print('Test #1 - inputs on neuron_1:', neuron_1.fire(inputs))
    print('Test #1 - inputs on neuron_2:', neuron_2.fire(inputs))
    print('Test #1 - inputs on neuron_3:', neuron_3.fire(inputs))
    print('Test #1 - inputs on neuron_4:', neuron_4.fire(inputs))