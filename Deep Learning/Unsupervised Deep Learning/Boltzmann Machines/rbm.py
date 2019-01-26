"""
Created on Sat Jan 19 2019

@author: Nodar Okroshiashvili
"""




# Bernuli Boltzmann Machines




# We are going to implement Restricted Boltzman Machines from scratch

# To optimize RBM we'll use "k-step contrastive divergence" algorithm



# Importing the libraries
import numpy as np
import pandas as pd
import torch
import torch.nn as nn # For Neural Networks
import torch.nn.parallel # For parallel computation
import torch.optim as optim # For optimization
import torch.utils.data # For data loading and preprocessing
from torch.autograd import Variable # For Stochastic Gradient Descet



# Importing the dataset

# Contains movie names and ganres
movies = pd.read_csv('data/ml-1m/movies.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')

# Contains user information
users = pd.read_csv('data/ml-1m/users.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')

# Contains movie ratings given by users
ratings = pd.read_csv('data/ml-1m/ratings.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')


# Preparing the training set and the test set

# Data is splitted by 80:20 rule
# 80% training set and 20% test set
# We converted data into Numpy array to build the model
training_set = pd.read_csv('data/ml-100k/u1.base', delimiter = '\t')
training_set = np.array(training_set, dtype = 'int')
test_set = pd.read_csv('data/ml-100k/u1.test', delimiter = '\t')
test_set = np.array(test_set, dtype = 'int')




# Getting the maximum number of users and movies
# We need these numbers to build RBM
nb_users = int(max(max(training_set[:,0]), max(test_set[:,0])))
nb_movies = int(max(max(training_set[:,1]), max(test_set[:,1])))



# Converting the data into an array with users in lines and movies in columns
# We create list of lists to make easy afterward to work with torch tensors
# First we make in this case 943 list because we have 943 users
# And each of these 943 lists will be a list of 1682 elements because
# we have 1682 movies
def convert(data):
    new_data = [] # initialize the list
    for id_users in range(1, nb_users + 1): # get rating for each user
        id_movies = data[:,1][data[:,0] == id_users] # movie id's 
        id_ratings = data[:,2][data[:,0] == id_users] # movie ratings
        ratings = np.zeros(nb_movies)
        ratings[id_movies - 1] = id_ratings
        new_data.append(list(ratings))
    return new_data


training_set = convert(training_set)
test_set = convert(test_set)



# Converting the data into Torch tensors
training_set = torch.FloatTensor(training_set)
test_set = torch.FloatTensor(test_set)



# Converting the ratings into binary ratings 1 (Liked) or 0 (Not Liked)
# So, we made input vector with three values
# -1 means user didn't watch the movie yet
# movies with rating 1 and 2 means user did not like them
# movies with rating more or equal to 3 means user liked it
training_set[training_set == 0] = -1 # user didn't watch the movie
training_set[training_set == 1] = 0 # user didn't like movie
training_set[training_set == 2] = 0 # user didn't like movie
training_set[training_set >= 3] = 1 # user liked movie

# Same for test set as in case of training set
test_set[test_set == 0] = -1
test_set[test_set == 1] = 0
test_set[test_set == 2] = 0
test_set[test_set >= 3] = 1



# Creating the architecture of the Neural Network
class RBM():
    def __init__(self, nv, nh): 
        """
        nv - # of visible nodes
        nh - # of hidden nodes
        """
        self.W = torch.randn(nh, nv) # initialize weights
        self.a = torch.randn(1, nh) # initialize bias for probabilities
                                    # of hidden nodes given visible nodes
        self.b = torch.randn(1, nv) # initialize bias for probabilities
                                    # of visible nodes given hidden nodes
    
    def sample_h(self, x):
        """
        samples the probabilities of the hidden nodes
        given the visible nodes
        
        X will correspond to the visible neurons V in the
        probabilities p(h|v)
        
        """
        wx = torch.mm(x, self.W.t()) # input times weights
        activation = wx + self.a.expand_as(wx) # we add bias
        p_h_given_v = torch.sigmoid(activation) # this is sigmoid activation
        return p_h_given_v, torch.bernoulli(p_h_given_v) 
        # returns probabilities and Gibbs sampling of hidden neurons
        # according to the probabilities
        # as we have binary outcome we use bernuli distribution
    
    
    def sample_v(self, y):
        """
        samples the probabilities of the visible nodes
        given the hidden nodes
        """
        wy = torch.mm(y, self.W)
        activation = wy + self.b.expand_as(wy)
        p_v_given_h = torch.sigmoid(activation)
        return p_v_given_h, torch.bernoulli(p_v_given_h)
    
    
    def train(self, v0, vk, ph0, phk):
        """
        Function for contrastive divergence
        
        It's too hard to compute gradient directly
        so we approximate it by contrastive divergence and
        this comes with Gibbs sampling
        
        Vector v0 contains the raitings of all the
        movies by one user
        
        vk is the visible node obtained after k samplings
        
        ph0 is the vector of probabilities that at the first
        iteration the hidden node equal one given the values of v0
        
        phk probabilities of the hidden nodes after k sampling
        given the values of the visible node vk
        """
        self.W += (torch.mm(v0.t(), ph0) - torch.mm(vk.t(), phk)).t()
        self.b += torch.sum((v0 - vk), 0)
        self.a += torch.sum((ph0 - phk), 0)


nv = len(training_set[0]) # number of movies or number of visible nodes
nh = 100 # number of hidden nodes or hidden features
batch_size = 100
# Batch size defines how fast the model is trained
# if batch size is 1 we have online learning and
# model learns very slow but makes much correct predictions
# This is hyper parameter

rbm = RBM(nv, nh) # RBM object



# Training the RBM
nb_epoch = 10  # number of epochs

for epoch in range(1, nb_epoch + 1):
    train_loss = 0
    """
    we need to normilize the loss function so 
    we need counter which is s
    """
    s = 0.
    
    for id_user in range(0, nb_users - batch_size, batch_size):
        vk = training_set[id_user:id_user+batch_size]
        v0 = training_set[id_user:id_user+batch_size] # Our target
        # v0 is freezed and we compare trained results to v0
        # and record error in train_loss variable
        # Loss function is: simple distance in absolute values
        # between prediction and real ratings
        ph0,_ = rbm.sample_h(v0)
        # ph0 computes the probabilities that the hidden node
        # equal 1 given the values of visible nodes in the original
        # input vector, that is given the original ratings
        for k in range(10): # for loop for k-steps of contrastive divergence
            _,hk = rbm.sample_h(vk)
            _,vk = rbm.sample_v(hk)
            vk[v0<0] = v0[v0<0] # freee cells that there are -1
            # They won't be updated during Gibb'sampling
        phk,_ = rbm.sample_h(vk)
        rbm.train(v0, vk, ph0, phk) # Apply train function
        # To update weights and bias
        train_loss += torch.mean(torch.abs(v0[v0>=0] - vk[v0>=0]))
        s += 1.
    print('epoch: '+str(epoch)+' loss: '+str(train_loss/s))
# From this setup I got the loss = 0.2471


# Testing the RBM
test_loss = 0
s = 0.
for id_user in range(nb_users):
    v = training_set[id_user:id_user+1]
    vt = test_set[id_user:id_user+1] # Target
    if len(vt[vt>=0]) > 0:
        _,h = rbm.sample_h(v)
        _,v = rbm.sample_v(h)
        test_loss += torch.mean(torch.abs(vt[vt>=0] - v[vt>=0]))
        s += 1.
print('test loss: '+str(test_loss/s))
# Test loss is 0.2407
# Model does not over or under fit


