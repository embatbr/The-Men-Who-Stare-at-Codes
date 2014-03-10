# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the Perceptron works.
"""


from neuron import signal, Neuron


class Perceptron(object):
    """Online learning Perceptron.
    """
    def __init__(self, input_size, lrn_rate=1, activation=signal):
        """'input_size' is the length of the input.
        'lrn_rate' is the learning rate.
        """
        self.neuron = Neuron([0]*input_size, 0, activation)
        self.lrn_rate = lrn_rate
        self.fire = self.neuron.fire

    def training(self, inputs_vector, outputs, max_epochs):
        """Not checking if inputs_vector and outputs have the same size.
        """
        epochs = 0

        while True:
            epochs = epochs + 1
            error_count = 0

            for (inputs, output) in zip(inputs_vector, outputs):
                actual_output = self.fire(inputs)
                error = output - actual_output

                if error != 0:
                    learned = self.lrn_rate*error
                    self.neuron.update(inputs, learned)
                    error_count = error_count + 1

            if error_count == 0:
                break
            elif max_epochs and (epochs > max_epochs):
                return False

        return epochs

    def __str__(self):
        ret = 'lrn_rate: %s' % self.lrn_rate
        ret = '%s\n%s' % (ret, self.neuron.__str__())
        return ret


class Layer(object):
    """A layer containing two or more perceptrons.
    """
    def __init__(self, input_size, num_perceptrons=2, lrn_rates=[1, 1],
                 activations=[signal, signal]):
        """Not checking if lrn_rates and activations have the length equals to
        num_perceptrons.
        """
        self.perceptrons = [Perceptron(input_size, lrn_rates[i], activations[i])
                            for i in range(num_perceptrons)]

    def fire(self, inputs):
        return [perceptron.fire(inputs) for perceptron in self.perceptrons]

    def training(self, inputs_vector, outputs_vector, max_epochs):
        """outputs_vector is a list containing the same number of elements of
        perceptron. Each element is another list with length equals to inputs_vector's
        length.
        """
        epochs = 0

        for (perceptron, outputs) in zip(self.perceptrons, outputs_vector):
            epochs_per_perceptron = perceptron.training(inputs_vector, outputs,
                                                        max_epochs)
            if not epochs_per_perceptron:
                return epochs_per_perceptron

            epochs = epochs + epochs_per_perceptron

        return epochs

    def __str__(self):
        ret = ''
        for (i, perceptron) in zip(range(len(self.perceptrons)), self.perceptrons):
            ret = '%sperceptron #%d:\n%s\n' % (ret, i, perceptron.__str__())
        return ret


def load_test(layer, inputs_vector, outputs_vector):
    error_count = 0
    desired_output_vector = [list(tup) for tup in zip(*outputs_vector)]

    for (inputs, desired_output) in zip(inputs_vector, desired_output_vector):
        actual_output = layer.fire(inputs)
        if desired_output != actual_output:
            error_count = error_count + 1

    return error_count


# test

from random import uniform


def classify(y, x, a, b):
    if y >= a*x + b:
        return 1 # class C1
    return -1 # class C2

def gen_examples(num_examples, a, b, c, d):
    inputs_vector = []
    outputs_vector = [[], []]

    for _ in range(num_examples):
        x1 = uniform(-10, 10)
        x2 = uniform(-10, 10)

        inputs_vector.append([x1, x2])
        outputs_vector[0].append(classify(x1, x2, a, b))
        outputs_vector[1].append(classify(x1, x2, c, d))

    return (inputs_vector, outputs_vector)

def layer(lrn_rates, num_training, num_test, a, b, c, d):
    layer = Layer(2, lrn_rates=lrn_rates)

    (inputs_vector, outputs_vector) = gen_examples(num_training, a, b, c, d)
    max_epochs = None
    print('#TRAINING%s' % (' (max_epochs = %d)' % max_epochs if max_epochs else ''))
    epochs = layer.training(inputs_vector, outputs_vector, max_epochs)
    print(('epochs: %d' % epochs) if epochs else 'training aborted')

    (inputs_vector, outputs_vector) = gen_examples(num_test, a, b, c, d)
    print('#TESTING')
    error_count = load_test(layer, inputs_vector, outputs_vector)
    print('error_count:', error_count)

if __name__ == '__main__':
    print('testing module perceptron')

    lrn_rates_list = [[x/10, x/10] for x in range(1, 11)]
    for lrn_rates in lrn_rates_list:
        print('\nlayer(%s, 10000, 1000, -5, 2, 3, 4)' % lrn_rates)
        layer(lrn_rates, 10000, 1000, -5, 2, 3, 4)

    # print('layer([1, 1], 10000, 1000, -5, 2, 3, 4)')
    # layer([1, 1], 10000, 1000, -5, 2, 3, 4)
