"""
Created on Sat Jan 26 2019

@author: Nodar Okroshiashvili
"""


# AutoEncoders




# Importing the libraries
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable

# Importing the dataset
movies = pd.read_csv('data/ml-1m/movies.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')
users = pd.read_csv('data/ml-1m/users.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')
ratings = pd.read_csv('data/ml-1m/ratings.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')

# Preparing the training set and the test set
training_set = pd.read_csv('data/ml-100k/u1.base', delimiter = '\t')
training_set = np.array(training_set, dtype = 'int')
test_set = pd.read_csv('data/ml-100k/u1.test', delimiter = '\t')
test_set = np.array(test_set, dtype = 'int')

# Getting the number of users and movies
nb_users = int(max(max(training_set[:,0]), max(test_set[:,0])))
nb_movies = int(max(max(training_set[:,1]), max(test_set[:,1])))


# Converting the data into an array with users in lines and movies in columns
def convert(data):
    new_data = []
    for id_users in range(1, nb_users + 1):
        id_movies = data[:,1][data[:,0] == id_users]
        id_ratings = data[:,2][data[:,0] == id_users]
        ratings = np.zeros(nb_movies)
        ratings[id_movies - 1] = id_ratings
        new_data.append(list(ratings))
    return new_data


training_set = convert(training_set)
test_set = convert(test_set)


# Converting the data into Torch tensors
training_set = torch.FloatTensor(training_set)
test_set = torch.FloatTensor(test_set)

"""
Till this point everything are the same as in Boltzman Machine case.

"""


# Creating the architecture of the Neural Network

# Class for Stacked AutoEncoders


class SAE(nn.Module): # In parenthesis there is parent class from pytorch
    def __init__(self, ): # this helps to initialize parameters when create SAE class object
        super(SAE, self).__init__() # "super" allow us to use functions
        # and methods from torch "Module"
        self.fc1 = nn.Linear(nb_movies, 20) # first full connection
        self.fc2 = nn.Linear(20, 10) # second full connection
        self.fc3 = nn.Linear(10, 20) # third full connection
        self.fc4 = nn.Linear(20, nb_movies) # output layer
        self.activation = nn.Sigmoid() # activation function
    def forward(self, x): # Function for forward propagation
        # x is our input vector or movie ratings
        x = self.activation(self.fc1(x)) # First encoding
        x = self.activation(self.fc2(x))
        x = self.activation(self.fc3(x))
        x = self.fc4(x) # vector of predicted ratings or decoding
        return x


sae = SAE() # SAE class object
criterion = nn.MSELoss() # Loss Function
optimizer = optim.RMSprop(sae.parameters(), lr = 0.01, weight_decay = 0.5)
# here, weight_decay parameter is used to reduce learning rate
# after every epoch. weight_decey = 0.5 means we take half of learning rate
# after each epoch to regulate convergence



# Training the SAE

nb_epoch = 200

for epoch in range(1, nb_epoch + 1): # for loop for epoch
    train_loss = 0
    s = 0.
    for id_user in range(nb_users): # for loop for each user
        input = Variable(training_set[id_user]).unsqueeze(0)
        target = input.clone()
        if torch.sum(target.data > 0) > 0:
            # This if condition is used to save memory
            # if user did not make any rating or put zeros
            # algorithm will not use this row while training
            output = sae(input) # output of predicted ratings
            
            target.require_grad = False # we don't require torch 
            # to compute gradient with respect to output
            output[target == 0] = 0
            loss = criterion(output, target) # RMSE loss
            mean_corrector = nb_movies/float(torch.sum(target.data > 0) + 1e-10)
            # this is average of the error but only considering
            # movies that were rated, movies with non-zero ratings
            loss.backward() # propagate loss backward
            train_loss += np.sqrt(loss.item() * mean_corrector)
            # mean_corrector is adjustment factor for loss
            s += 1.
            optimizer.step()
            # backward decides the direction to which the weights will be updated
            # that is they will increase or decrease
            # optimizer step decides the intensity of the updates.
            # that is the amount b which weights will be updated
    print('epoch: '+str(epoch)+' loss: '+str(train_loss/s))
    
# if final loss is, say 1 this means that on average our model makes
# one star error. In  other words, if user gave 4 star rating, predicted
# rating may be 5 or 3


# Train loss is equal to 0.91084



# Testing the SAE
test_loss = 0
s = 0.

for id_user in range(nb_users):
    input = Variable(training_set[id_user]).unsqueeze(0)
    target = Variable(test_set[id_user]).unsqueeze(0)
    if torch.sum(target.data > 0) > 0:
        output = sae(input)
        target.require_grad = False
        output[target == 0] = 0
        loss = criterion(output, target)
        mean_corrector = nb_movies/float(torch.sum(target.data > 0) + 1e-10)
        test_loss += np.sqrt(loss.item() * mean_corrector)
        s += 1.
print('test loss: '+str(test_loss/s))

# Test loss equal to 0.95607


