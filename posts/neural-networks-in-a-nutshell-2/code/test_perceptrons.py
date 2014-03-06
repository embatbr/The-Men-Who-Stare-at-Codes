# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to test perceptrons.
"""


from random import uniform
from perceptrons import Perceptron, load_test, validate


def gen_examples(num_examples, a, b):
    examples = []

    for _ in range(num_examples):
        x1 = uniform(-1, 1)
        x2 = uniform(-1, 1)
        example = ([x1, x2], __classify__(x1, x2, a, b))
        examples.append(example)

    return examples

def __classify__(y, x, a, b):
    if y >= a*x + b:
        return 1 # class C1
    return -1 # class C2

def perceptron(lrn_rate, epochs, training, validation, max_error, test, a, b):
    """max_error = 0.xy == xy%
    """
    perceptron = Perceptron(2, lrn_rate)

    training_examples = gen_examples(training, a, b)
    print('#training')
    perceptron.train(training_examples, epochs)

    validation_examples = gen_examples(validation, a, b)
    print('#validating')
    valid = validate(perceptron, validation_examples, max_error)
    print('valid?', valid[0])
    print('error:', valid[1])

    test_examples = gen_examples(test, a, b)
    print('#testing')
    error = load_test(perceptron, test_examples)
    print('error:', error)


if __name__ == '__main__':
    # maxError: xy, where it's xy% or 0.xy

    print('perceptron(1, 1, 100, 100, 0.12, 10, -5, 2)')
    perceptron(1, 1, 100, 100, 0.12, 10, -5, 2)

    print('\nperceptron(1, 10, 300, 300, 0.08, 100, -5, 2)')
    perceptron(1, 10, 300, 300, 0.08, 100, -5, 2)

    print('\nperceptron(0.3, 100, 1000, 1000, 0.005, 100, -5, 2)')
    perceptron(0.3, 100, 1000, 1000, 0.005, 100, -5, 2)