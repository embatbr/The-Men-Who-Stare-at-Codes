# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the Multilayer Perceptron works.
"""


from neuron import logsig, tansig, Neuron


class NeuralLayer(object):
    """A layer of independent neurons, all with the same activation function.
    """
    def __init__(self, num_neurons, input_size, activation):
        self.neurons = []
        for i in range(num_neurons):
            neuron = Neuron([0]*input_size, 0, activation)
            self.neurons.append(neuron)

    def fire(self, input_vector):
        """Not checking if input_vector fits in the neurons' inputs.
        """
        return [neuron.fire(input_vector) for neuron in self.neurons]

    def __str__(self):
        ret = ''
        num_neurons = len(self.neurons)
        for (neuron, i) in zip(self.neurons, range(num_neurons)):
            ret = '%sneuron #%d\n%s\n' % (ret, i, neuron.__str__())
        return ret


class MultilayerPerceptron(object):
    """A feedfoward neural network composed of N neural layers (1 output layer
    and N - 1 hidden layers) plus a input layer.
    """
    def __init__(self, num_neurons_per_layer, input_size, activation, lrn_rate):
        """num_neurons_per_layer is a list of int.
        """
        num_inputs_per_layer = [input_size] + num_neurons_per_layer[: -1]
        num_layers = len(num_neurons_per_layer)

        self.layers = []
        for i in range(num_layers):
            layer = NeuralLayer(num_neurons_per_layer[i],
                                num_inputs_per_layer[i], activation)
            self.layers.append(layer)

        self.lrn_rate = lrn_rate

    def fire(self, input_vector):
        """Foward pass.
        """
        output = input_vector
        for layer in self.layers:
            output = layer.fire(output)
        return output

    def training(self, training_examples, validation_examples):
        """The training is made using cross-validation. For each epoch there's a
        validation, and the MSE is monitored, so the training stops in case it
        starts to raise.
        """
        training_size = len(training_examples)
        validation_size = len(validation_examples)
        old_mse_valid = None

        while True:
            # training
            mse_train = 0
            for (input_vector, desired) in training_examples:
                actual_output = mlp.fire(input_vector)
                error = sum([(d - y)*(d - y) for (d, y) in
                             zip(desired_output, actual_output)])
                mse_train = mse_train + error/2

            mse_train = mse_train/training_size

            # validation
            mse_valid = 0
            for (input_vector, desired) in validation_examples:
                output = self.fire(input_vector)
                error = desired - output
                mse_valid = mse_valid + error*error
            mse_valid = mse_valid/(2 * validation_size)

            if not old_mse_valid:
                old_mse_valid = mse_valid
            elif mse_valid < old_mse_valid:
                old_mse_valid = mse_valid
            elif mse_valid > old_mse_valid:
                return (mse_train, mse_valid)

    def __str__(self):
        ret = ''
        num_layers = len(self.layers)
        for (layer, i) in zip(self.layers, range(num_layers)):
            ret = '%slayer #%d\n%s\n' % (ret, i, layer.__str__())
        return ret


def load_test(mlp, testing_examples):
    mse_test = 0

    for (input_vector, desired_output) in testing_examples:
        actual_output = mlp.fire(input_vector)
        error = sum([d - y for (d, y) in zip(desired_output, actual_output)])
        mse_test = mse_test + (error*error)

    testing_size = len(testing_examples)
    mse_test = mse_test/(2 * testing_size()

    return mse_test

# test

from random import uniform, random


# classifies a input similar to the perceptron, with a probability of being wrong
def classify(y, x, a, b, c, d, prob_wrong=0.2):
    wrong = random() < prob_wrong
    classification = 1 # class C1

    if (y < a*x + b) or (y < c*x + d):
        classification =  -1 # class C2

    if wrong:
        classification = -classification
    return classification

def gen_examples(num_examples, a, b, c, d):
    examples = []

    for _ in range(num_examples):
        x1 = uniform(-10, 10)
        x2 = uniform(-10, 10)
        examples.append(([x1, x2], classify(x1, x2, a, b, c, d)))

    return examples