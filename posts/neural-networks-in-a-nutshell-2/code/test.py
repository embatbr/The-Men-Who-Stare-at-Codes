#!/usr/bin/python3.3
# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to test perceptrons.
"""


from random import uniform
from neuron import *
from perceptrons import Perceptron, load_test


def gen_examples(num_examples, a, b):
    examples = []

    for _ in range(num_examples):
        x1 = uniform(-10, 10)
        x2 = uniform(-10, 10)
        example = ([x1, x2], __classify__(x1, x2, a, b))
        examples.append(example)

    return examples

def __classify__(y, x, a, b):
    if y >= a*x + b:
        return 1 # class C1
    return -1 # class C2

def perceptron(lrn_rate, num_training, num_test, a, b):
    perceptron = Perceptron(2, lrn_rate)

    training_examples = gen_examples(num_training, a, b)
    print('#TRAINING')
    epochs = perceptron.training(training_examples)
    print('epochs:', epochs)

    test_examples = gen_examples(num_test, a, b)
    print('#TESTING')
    error_count = load_test(perceptron, test_examples)
    print('error_count:', error_count)


if __name__ == '__main__':
    import sys

    params = sys.argv[1 : ]
    if params[0] == 'neuron':
        print('testing module neuron\n')

        neuron_1 = Neuron([0.4, 0.6, 0.9], -0.8)
        neuron_2 = Neuron([0.4, 0.6, 0.9], -1.5, signal)
        neuron_3 = Neuron([0.4, 0.6, 0.9], -0.8, logsig)
        neuron_4 = Neuron([0.4, 0.6, 0.9], -0.8, tansig)

        print('neuron_1:', neuron_1, sep='\n')
        print('\nneuron_2:', neuron_2, sep='\n')
        print('\nneuron_3:', neuron_3, sep='\n')
        print('\nneuron_4:', neuron_4, sep='\n')

        inputs = [1, 0, 1]
        print('\nTest #1 - inputs on neuron_1:', neuron_1.fire(inputs))
        print('Test #1 - inputs on neuron_2:', neuron_2.fire(inputs))
        print('Test #1 - inputs on neuron_3:', neuron_3.fire(inputs))
        print('Test #1 - inputs on neuron_4:', neuron_4.fire(inputs))

    if params[0] == 'perceptron':
        print('testing module perceptron\n')

        lrn_rate_list = [x/10 for x in range(1, 11)]
        for lrn_rate in lrn_rate_list:
            print('perceptron(%s, 10000, 1000, -5, 2)' % lrn_rate)
            perceptron(lrn_rate, 10000, 1000, -5, 2)
