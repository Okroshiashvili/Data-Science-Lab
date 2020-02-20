


"""
Thompson Sampling Algorithm

"""



# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt


# Import the dataset
dataset = pd.read_csv('data/Ads_CTR_Optimisation.csv')

"""

First, let implement Random Selection as a baseline and then implement
Thompson Sampling to compare with.

"""



# Random Selection

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
    reward = dataset.values[n, ad] # add here corresponds index at which ad was selected
    if reward == 1:
       numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward        


# Visualize the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ads was selected')
plt.show()




"""
We see that, while using Random Selection, the reward is about 1200.
Using Thompson Sampling gives us reward around 2500, such an improvement.

"""


