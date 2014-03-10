# -*- coding: utf-8 -*-


"""author: Eduardo Tenório (embatbr@gmail.com)
The Men Who Stare at Codes (themenwhostareatcodes.wordpress.com)

This code is intended to teach how the Adaline works.
"""


def limited_linear(x):
    if x > 1:
        return 1
    elif x < -1:
        return -1
    return x


class Adaline():
    """Online learning Adaline.
    """
    def __init__(self, input_size, lrn_rate=1):
        """'input_size' is the length of the input.
        'lrn_rate' is the learning rate.
        """
        self.weights = [0]*input_size
        self.bias = 0
        self.lrn_rate = lrn_rate

    def fire(self, input_vector):
        summed = sum([i*w for (i,w) in zip(input_vector, self.weights)])
        return limited_linear(summed + self.bias)


    def training(self, training_examples, validation_examples):
        validation_size = len(validation_examples)
        old_mse = None

        while True:
            # training
            for (input_vector, desired) in training_examples:
                output = self.fire(input_vector)
                error = desired - output

                if error != 0:
                    delta = self.lrn_rate*error
                    self.weights = [(weight + delta*x) for (weight, x) in
                                    zip(self.weights, input_vector)]
                    self.bias = self.bias + delta

            # validation
            mse = 0
            for (input_vector, desired) in validation_examples:
                output = self.fire(input_vector)
                error = desired - output
                mse = mse + error*error
            mse = mse/validation_size

            if not old_mse:
                old_mse = mse
            elif mse < old_mse:
                old_mse = mse
            elif mse > old_mse:
                return mse

    def __str__(self):
        ret = 'lrn_rate: %s' % self.lrn_rate
        ret = '%s\nweights: %s' % (ret, str(self.weights))
        ret = '%s\nbias: %s' % (ret, self.bias)
        return ret


def load_test(adaline, testing_examples):
    testing_size = len(testing_examples)
    mse = 0
    for (input_vector, desired_output) in testing_examples:
        actual_output = adaline.fire(input_vector)
        error = desired_output - actual_output
        mse = mse + error*error
    mse = mse/testing_size

    return mse

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

def adaline(lrn_rate, num_training, num_validation, num_test, a, b):
    adaline = Adaline(2, lrn_rate=lrn_rate)

    training_examples = gen_examples(num_training, a, b)
    validation_examples = gen_examples(num_validation, a, b)
    print('TRAINING')
    mse = adaline.training(training_examples, validation_examples)
    print('mse:', mse)

    testing_examples = gen_examples(num_test, a, b)
    print('\nTESTING')
    mse = load_test(adaline, testing_examples)
    print('mse:', mse)

    print('\nADALINE:')
    print(adaline)

if __name__ == '__main__':
    print('testing module adaline\n')

    # lrn_rate_list = [x/10 for x in range(1, 11)]
    # for lrn_rate in lrn_rate_list:
    #     print('adaline(%s, 10000, 10000, 1000, -5, 2):\n' % lrn_rate)
    #     adaline(lrn_rate, 10000, 10000, 1000, -5, 2)

    print('testing')
    adaline(0.1, 10000, 10000, 1000, -5, 2)
