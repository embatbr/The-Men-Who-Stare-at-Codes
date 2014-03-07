# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the Perceptron works.
"""


from neuron import signal, Neuron


class Perceptron():

    def __init__(self, input_size, weights=None, bias=0, activation=signal,
                 lrn_rate=1):
        """'input_size' is the length of the input.
        'lrn_rate' is the learning rate.
        """
        if not weights:
            weights = [0]*input_size
        self.neuron = Neuron(weights, bias, activation)
        self.lrn_rate = lrn_rate
        self.fire = self.neuron.fire

    def training(self, examples):
        epochs = 0

        while True:
            epochs = epochs + 1
            error_count = 0

            for (input_vector, desired_output) in examples:
                actual_output = self.neuron.fire(input_vector)
                error = desired_output - actual_output

                if error != 0:
                    learned = self.lrn_rate*error
                    self.neuron.update(input_vector, learned)
                    error_count = error_count + 1

            if error_count == 0:
                break

        return epochs

    def __str__(self):
        ret = 'lrn_rate: %s' % self.lrn_rate
        ret = '%s\n%s' % (ret, neuron.__str__())
        return ret


def load_test(perceptron, examples):
    error_count = 0

    for (input_vector, desired_output) in examples:
        actual_output = perceptron.fire(input_vector)
        if desired_output != actual_output:
            error_count = error_count + 1

    return error_count


# test

from random import uniform


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

if __name__ == '__main__':
    print('testing module perceptron\n')

    lrn_rate_list = [x/10 for x in range(1, 11)]
    for lrn_rate in lrn_rate_list:
        print('perceptron(%s, 10000, 1000, -5, 2)' % lrn_rate)
        perceptron(lrn_rate, 10000, 1000, -5, 2)
