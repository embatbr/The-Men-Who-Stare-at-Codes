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

    def load_test(self, examples):
        total = len(examples)
        error = 0
        for example in examples:
            (input_vector, desired_output) = example
            actual_output = self.fire(input_vector)
            if desired_output != actual_output:
                error = error + 1

        return error/total

    def validate(self, examples, max_error):
        error = self.load_test(examples)
        return (max_error > error, error)

    def __str__(self):
        ret = super().__str__()

        return ret


# Tests

def __classify__(y, x, a, b):
    if y >= a*x + b:
        return 1 # class C1
    return -1 # class C2

if __name__ == '__main__':
    import sys, json, os, os.path
    from random import choice, uniform

    params = sys.argv[1 : ]
    # params: lrn_rate epochs num_training num_validation max_error num_test a b
    # from 'y = a*x + b'
    lrn_rate = float(params[0])
    epochs = int(params[1])
    num_training = int(params[2])
    num_validation = int(params[3])
    max_error = float(params[4])
    num_test = int(params[5])
    a = float(params[6])
    b = float(params[7])

    perceptron = Perceptron(2, lrn_rate)

    print('PRE-TRAINING:\n', perceptron, sep='')

    examples = []
    for _ in range(num_training):
        x1 = uniform(-1, 1)
        x2 = uniform(-1, 1)
        example = ([x1, x2], __classify__(x1, x2, a, b))
        examples.append(example)

    print('\ntraining')
    perceptron.train(examples, epochs)
    print('\nPOS-TRAINING:\n', perceptron, sep='')

    examples = []
    for _ in range(num_validation):
        x1 = uniform(-1, 1)
        x2 = uniform(-1, 1)
        example = ([x1, x2], __classify__(x1, x2, a, b))
        examples.append(example)

    print('\nvalidating')
    validation_error = perceptron.validate(examples, max_error)

    examples = []
    for _ in range(num_test):
        x1 = uniform(-1, 1)
        x2 = uniform(-1, 1)
        example = ([x1, x2], __classify__(x1, x2, a, b))
        examples.append(example)

    print('\ntesting')
    test_error = perceptron.load_test(examples)

    # name: perceptron_lrnRate_epochs_numExamples_a_b
    # format: weights bias activation
    nethash = hash(perceptron)
    filename = 'nets/trained_net_%s.json' % nethash
    if not os.path.exists('nets'):
        os.makedirs('nets')
    with open(filename, 'w') as netfile:
        net_params = {'type' : 'perceptron', 'lrn_rate' : lrn_rate,
                      'epochs' : epochs, 'num_training' : num_training,
                      'num_validation' : num_validation, 'num_test' : num_test,
                      'max_error' : max_error, 'a' : a, 'b' : b}
        net_attr = {'bias' : perceptron.bias, 'weights' : perceptron.weights,
                    'activation' : perceptron.activation.__name__,
                    'lrn_rate' : perceptron.lrn_rate}
        net = {'net_params' : net_params, 'net_attr' : net_attr,
               'validation_error' : validation_error, 'test_error' : test_error}
        netfile.write(json.dumps(net, indent=4, sort_keys=True))

    print('\nsaved on', filename)
