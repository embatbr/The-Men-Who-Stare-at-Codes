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

    def __str__(self):
        ret = ''
        num_layers = len(self.layers)
        for (layer, i) in zip(self.layers, range(num_layers)):
            ret = '%slayer #%d\n%s\n' % (ret, i, layer.__str__())
        return ret


mlp = MultilayerPerceptron([4, 5, 2], 3, logsig, 0.1)
print(mlp)
print('fire:', mlp.fire([1, -1, 1]))
