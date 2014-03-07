#!/usr/bin/python3.3
# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to test perceptrons.
"""


from random import uniform
from neuron import *
from perceptrons import Perceptron, load_test


def classify(y, x, a, b):
    if y >= a*x + b:
        return 1 # class C1
    return -1 # class C2

def gen_examples(num_examples, a, b):
    examples = []

    for _ in range(num_examples):
        x1 = uniform(-10, 10)
        x2 = uniform(-10, 10)
        examples.append(([x1, x2], classify(x1, x2, a, b)))

    return examples

def perceptron(lrn_rate, num_training, num_test, a, b):
    perceptron = Perceptron(2, lrn_rate=lrn_rate)

    examples = gen_examples(num_training, a, b)
    print('#TRAINING')
    epochs = perceptron.training(examples)
    print('epochs:', epochs)

    examples = gen_examples(num_test, a, b)
    print('#TESTING')
    error_count = load_test(perceptron, examples)
    print('error_count:', error_count)



