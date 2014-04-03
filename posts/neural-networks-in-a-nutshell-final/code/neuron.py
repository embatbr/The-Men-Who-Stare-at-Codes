# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to show how to define and use a general model of a neuron.
"""


from math import exp, tanh


# Activation functions

def treshold(x):
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

# TODO criar funções de diferenciação para logsig e tansig, bem como uma 'diff' geral


# Classes

class Neuron(object):

    def __init__(self, weights, bias, activation=treshold):
        self.weights = weights
        self.bias = bias
        self.activation = activation

    def fire(self, input_vector):
        summed = sum([i*w for (i,w) in zip(input_vector, self.weights)])
        return self.activation(summed + self.bias)

    def update(self, input_vector, factor):
        self.weights = [(w + factor*x) for (w, x) in
                        zip(self.weights, input_vector)]
        self.bias = self.bias + factor # x = +1

    def __str__(self):
        ret = 'weights: %s' % str(self.weights)
        ret = '%s\nbias: %s' % (ret, self.bias)
        ret = '%s\nactivation: %s' % (ret, self.activation.__name__)

        return ret
