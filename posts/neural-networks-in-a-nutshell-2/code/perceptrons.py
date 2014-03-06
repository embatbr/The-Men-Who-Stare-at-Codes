# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the many kinds of Perceptrons work.
"""


from neuron import signal, Neuron


class Perceptron(Neuron):

    def __init__(self, input_size, lrn_rate=1, weights=None, bias=0):
        """'input_size' is the length of the input.
        'lrn_rate' is the learning rate.
        """
        if not weights:
            weights = [0]*input_size
        super().__init__(weights, bias, signal)
        self.lrn_rate = lrn_rate

    def train(self, examples, epochs=1):
        """'examples' is a list of tuples (input_vector, desired_output)
        """
        for i in range(epochs):
            for example in examples:
                (input_vector, desired_output) = example
                actual_output = self.fire(input_vector)
                error = desired_output - actual_output

                self.weights = [(w + self.lrn_rate*error*x) for (w, x) in
                                zip(self.weights, input_vector)]
                self.bias = self.bias + self.lrn_rate*error

    def __str__(self):
        ret = super().__str__()

        return ret

def load_test(perceptron, examples):
    total = len(examples)
    error = 0
    for example in examples:
        (input_vector, desired_output) = example
        actual_output = perceptron.fire(input_vector)
        if desired_output != actual_output:
            error = error + 1

    return error/total

def validate(perceptron, examples, max_error):
    error = load_test(perceptron, examples)
    return (max_error > error, error)
