# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the Perceptron works.
"""


from neuron import signal, Neuron


class Perceptron():
    """A layer with one or more neurons.
    """

    def __init__(self, input_size, weights=None, bias=None, activation=signal,
                 lrn_rate=1, num_neurons=1):
        """'input_size' is the length of the input.
        'lrn_rate' is the learning rate.
        """
        if not weights and not bias:
            weights = [[0]*input_size]*num_neurons
            bias = [0]*num_neurons

        self.neurons = [Neuron(weights[i], bias[i], activation) for i in
                        range(num_neurons)]
        self.lrn_rate = lrn_rate
        self.num_neurons = num_neurons

    def fire(self, input_vector):
        return [neuron.fire(input_vector) for neuron in self.neurons]

    def training(self, examples, max_epochs=None):
        epochs = 0

        while True:
            epochs = epochs + 1
            error_count = 0

            for (input_vector, desired_output_vector) in examples:
                for i in range(self.num_neurons):
                    neuron = self.neurons[i]
                    desired_output = desired_output_vector[i]
                    actual_output = neuron.fire(input_vector)
                    error = desired_output - actual_output

                    if error != 0:
                        learned = self.lrn_rate*error
                        neuron.update(input_vector, learned)
                        error_count = error_count + 1

            if error_count == 0:
                return epochs
            elif max_epochs and (epochs > max_epochs):
                return False

    def __str__(self):
        ret = 'lrn_rate: %s' % self.lrn_rate
        for i in range(self.num_neurons):
            neuron = self.neurons[i]
            ret = '%s\nneuron #%d:\n%s' % (ret, i, neuron.__str__())
        return ret


def load_test(perceptron, examples):
    error_count = 0

    for (input_vector, desired_output_vector) in examples:
        actual_output_vector = perceptron.fire(input_vector)
        if desired_output_vector != actual_output_vector:
            error_count = error_count + 1

    return error_count


# test for 2 neurons

from random import uniform


def classify(y, x, a, b, c, d):
    if (y >= a*x + b) and (y >= c*x + d):
        return [1, 1] # class C1
    elif (y >= a*x + b) and (y < c*x + d):
        return [1, -1] # class C2
    elif (y < a*x + b) and (y >= c*x + d):
        return [-1, 1] # class C3
    return [-1, -1] # class C4

def gen_examples(num_examples, a, b, c, d):
    examples = []

    for _ in range(num_examples):
        x1 = uniform(-10, 10)
        x2 = uniform(-10, 10)
        examples.append(([x1, x2], classify(x1, x2, a, b, c, d)))

    return examples

def perceptron(lrn_rate, num_training, num_test, a, b, c, d):
    perceptron = Perceptron(2, lrn_rate=lrn_rate, num_neurons=2)

    examples = gen_examples(num_training, a, b, c, d)
    print('#TRAINING (max_epochs = 80)')
    epochs = perceptron.training(examples, max_epochs=80)
    print('epochs:', epochs if epochs else 'NOT TRAINED')

    if epochs:
        examples = gen_examples(num_test, a, b, c, d)
        print('#TESTING')
        error_count = load_test(perceptron, examples)
        print('error_count:', error_count)

if __name__ == '__main__':
    print('testing module perceptron')

    lrn_rate_list = [x/10 for x in range(1, 11)]
    for lrn_rate in lrn_rate_list:
        print('\nperceptron(%s, 10000, 1000, -5, 2, 3, 4)' % lrn_rate)
        perceptron(lrn_rate, 10000, 1000, -5, 2, 3, 4)
