# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to show how to define and use a McCulloch-Pitts neuron.
"""


def threshold(x):
    if x >= 0:
        return 1
    else:
        return 0


class MCP_Neuron(object):

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def fire(self, inputs):
        summed = sum([i*w for (i,w) in zip(inputs, self.weights)])
        return threshold(summed + self.bias)


if __name__ == '__main__':
    neuron_1 = MCP_Neuron([0.2, 0.7, 0.3], -1.5)
    neuron_2 = MCP_Neuron([0.4, 0.6, 0.9], -0.8)
    neuron_3 = MCP_Neuron([0.7, 0.4, -0.9], -0.6)

    inputs = [1, 0, 1]

    print('Test #1 - inputs on neuron_1:', neuron_1.fire(inputs))
    print('Test #1 - inputs on neuron_2:', neuron_2.fire(inputs))
    print('Test #1 - inputs on neuron_3:', neuron_3.fire(inputs))