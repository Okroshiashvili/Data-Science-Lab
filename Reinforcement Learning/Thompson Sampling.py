"""
Created on Sun Mar 11 17:23:39 2018

@author:  Nodar.Okroshiashvili 
"""
#%%

"""

Thompson Samplin Algorithm

"""

#%%

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Import the dataset
dataset = pd.read_csv('data/Ads_CTR_Optimisation.csv')


#%%

# Implement Random Selection


import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

# Visualizing the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

#%%

# Implement Thompson Sampling Algorithm from scratch


import random

N = 10000  # Number of rounds
d = 10     # Number of versions of ad
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d  # Initialize these two variables
total_reward = 0
for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
 # Generates random draws       
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1,numbers_of_rewards_0[i] + 1 )

        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad] # ad here corresponds index at whcih ad was selected
    if reward == 1:
       numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward        


#%%


# Visualize the results

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ads was selected')
plt.show()


#%%

