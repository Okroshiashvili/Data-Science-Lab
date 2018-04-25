"""
Created on Sun Mar  4 15:54:04 2018

@author: Nodar.Okroshiashvili
"""
#%%

"""

Upper Confidence Bound

"""

#%%

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Import the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#%%

"""
Each time a user connects to the network we display one version of ten ads 
totally randomly.

Here we implement Random Selection which can be considered with the primitive 
equivalent of UCB. In total Random Selection Algorithm produced 1200
reward on average

"""

import random

N = 10000
d = 10

ads_selected = []
total_rewards = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_rewards = total_rewards + reward
# sum of the rewards ot to the last round
    
# Visualize the results of Random Selection

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

#%%

# Now let see how Random Selection algorithm is going to compared with UCB

# Implement UCB Algorithm from scratch



# We need to declare two variables N and R

import math
N = 10000  # Number of rounds
d = 10     # Number of versions of ad
ads_selected = []
number_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
for n in range(0, N):
    max_upper_bound = 0
    ad = 0
    for i in range(0, d):
        if (number_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1)/ number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward        
"""
During first ten rounds the ten ads are selected and then
our strategy starts to work.

More specifically at round zero ad zero is selected, at round one 
ad one is selected and so on until round nine, after that since we have some 
information about the sums of rewards and the numbers of selections.


If we take look at ads_selected we notice that ad version 4 is optimal and at 
the last thousands steps, only 4 is chosen, but as python index starts at 
zero this corresponds to the ad version 5(five).

"""

#%%


# Visualize the results

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ads was selected')
plt.show()

#%%