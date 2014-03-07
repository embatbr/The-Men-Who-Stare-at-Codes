# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the many kinds of Perceptrons work.
"""


from neuron import signal, Neuron


class Perceptron():

    def __init__(self, input_size, lrn_rate=1, weights=None, bias=0,
                 activation=signal):
        """'input_size' is the length of the input.
        'lrn_rate' is the learning rate.
        """
        if not weights:
            weights = [0]*input_size
        self.neuron = Neuron(weights, bias, activation)
        self.lrn_rate = lrn_rate

    def training(self, examples):
        epochs = 0
        while True:
            epochs = epochs + 1
            error_count = 0

            for example in examples:
                (input_vector, desired_output) = example
                actual_output = self.fire(input_vector)
                error = desired_output - actual_output

                if error != 0:
                    learned = self.lrn_rate*error
                    self.neuron.weights = [(w + learned*x) for (w, x) in
                                           zip(self.neuron.weights, input_vector)]
                    self.neuron.bias = self.neuron.bias + learned # x = +1

                    error_count = error_count + 1

            if error_count == 0:
                break

        return epochs

    def fire(self, input_vector):
        return self.neuron.fire(input_vector)

    def __str__(self):
        ret = self.neuron.__str__()
        ret = '%s\n%s' % (ret, self.lrn_rate)

        return ret

def load_test(perceptron, examples):
    error_count = 0
    for example in examples:
        (input_vector, desired_output) = example
        actual_output = perceptron.fire(input_vector)
        if desired_output != actual_output:
            error_count = error_count + 1

    return error_count
