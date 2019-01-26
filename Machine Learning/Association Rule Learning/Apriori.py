"""
Created on Mon Feb 26 09:58:08 2018

@author: Nodar.Okroshiashvili
"""
#%%

"""

Apriori

"""

#%%

# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("data/Market_Basket_Optimisation.csv", header= None)


# Apriori algorithm expects list of lists as input and they must be strings
# We need to convert dataframe into list of lists

# We need two for loop

# this loop goes to all the transactions
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])
    
# Here i goes to all index and j goes to all column and extracts values for i    
    
#%%

# Apply Apriori to the dataset

from apyori import apriori


# Apriori function takes transactions as inputs and gives rules as outputs
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# min_support = 3 * 7 / 7500 three products bought 3 times a day time 7 for week adnover 7500
# min_confidence = 80% / 2 = 40% / 2 = 20% 
# min_lift = we need rules that have lift at least three


#%%

# Visualize the results and rules

results = list(rules)

# Rules found by the algorithm are already sorted by the relevance or by the decreasing lift

results_list = []
for i in range(0, len(results)):
    results_list.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]) + '\n' + str(results[i][2]))
  
myResults = [list(x) for x in results]

#%%
