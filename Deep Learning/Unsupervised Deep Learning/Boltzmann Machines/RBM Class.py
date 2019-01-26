"""
Created on Sat Jan 19 15:27:41 2019

@author: nodo
"""


"""
I wrote this class for Boltzman Machine and going to rewrite
main class in rbm.py file to be more understandable
"""







class RestrictedBoltzmannMachine():
    def __init__(self, visible_node_count, hidden_node_count):        
        # initialise weights (synapses/connections) and individual node biases with normal distributed rands
        self.connection_weights = torch.randn(hidden_node_count, visible_node_count)
        self.hidden_node_bias   = torch.randn(1, hidden_node_count)
        self.visible_node_bias  = torch.randn(1, visible_node_count)
 
    def sample_hidden_nodes(self, x_visible_node_input_values):
        # get product of [input neurons]•[Weights.transpose()]
        #   transpose is needed to rotate the weights matrix to have the visible nodes ias columns
        #   - the same orientation as the input values
        weighted_input = torch.mm(x_visible_node_input_values, self.connection_weights.t())
        # create activation value by adding the [hidden node] bias to the weighted input 
        #   where hidden node bias (expanded to the shape of the the weighted inputs) 
        values_for_activation = weighted_input + self.hidden_node_bias.expand_as(weighted_input)
 
        # caluclate probability of hidden node activation for given visible node weight
        activation_probablilities = torch.sigmoid(values_for_activation)
 
        # Bernoulli sampling involves generating a random number between 0 and 1 then 
        # returning a 1 if the rand <= activation_probability (to activate the neuron (100*prob)% of the time)
        return activation_probablilities, torch.bernoulli(activation_probablilities)
    
 
