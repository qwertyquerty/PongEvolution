import numpy as np
import random

@np.vectorize
def sigmoid(x):
    return 1 / (1 + np.e ** -x)

activation_function = sigmoid

from scipy.stats import truncnorm
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

class Neural_Network:
    def __init__(self, no_of_in_nodes, no_of_out_nodes, no_of_hidden_nodes, learning_rate, bias=None):
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.learning_rate = learning_rate
        self.bias = bias
        self.create_weight_matrices()

    def create_weight_matrices(self):
        bias_node = 1 if self.bias else 0
        rad = 1 / np.sqrt(self.no_of_in_nodes + bias_node)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes,self.no_of_in_nodes + bias_node))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes + bias_node)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes,self.no_of_hidden_nodes + bias_node))


    def run(self, input_vector):
        if self.bias:
            input_vector = np.concatenate( (input_vector, [1]) )
        input_vector = np.array(input_vector, ndmin=2).T
        output_vector = np.dot(self.weights_in_hidden, input_vector)
        output_vector = activation_function(output_vector)
        if self.bias:
            output_vector = np.concatenate( (output_vector, [[1]]) )
        output_vector = np.dot(self.weights_hidden_out, output_vector)
        output_vector = activation_function(output_vector)

        return output_vector

    def copy(self):
        n = Neural_Network(self.no_of_in_nodes, self.no_of_out_nodes, self.no_of_hidden_nodes, self.learning_rate, self.bias)
        n.weights_in_hidden = self.weights_in_hidden.copy()
        n.weights_hidden_out = self.weights_hidden_out.copy()
        return n

    def mutate(self,rate):
        for x,y in np.ndindex(self.weights_in_hidden.shape):
            self.weights_in_hidden[x,y] += round(random.random()*rate,7)
            if random.randint(0,5) == 0:
                self.weights_in_hidden[x,y] *= -1
        for x,y in np.ndindex(self.weights_hidden_out.shape):
            self.weights_hidden_out[x,y] += round(random.random()*rate,7)
            if random.randint(0,5) == 0:
                self.weights_hidden_out[x,y] *= -1
