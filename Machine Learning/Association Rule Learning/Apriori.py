


"""
Apriori

"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from apyori import apriori

dataset = pd.read_csv("data/Market_Basket_Optimisation.csv", header= None)


# Apriori algorithm expects list of lists as input and they must be strings
# We need to convert dataframe into list of lists


# this loop goes to all the transactions
n = len(dataset)

transactions = []

for i in range(0, n):
    transaction = []
    m = len(dataset.values[i])
    for j in range(0, m):
        data = str(dataset.values[i,j])
        if data != "nan":
            transaction.append(data)
            transactions.append(transaction)


# Apply Apriori to the dataset

# Apriori function takes transactions as inputs and gives rules as outputs
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# min_support = 3 * 7 / 7500 three products bought 3 times a day time 7 for week and over 7500
# min_confidence = 80% / 2 = 40% / 2 = 20% 
# min_lift = we need rules that have lift at least three




# Visualize the results and rules

results = list(rules)

# Rules found by the algorithm are already sorted by the relevance or by the decreasing lift

results_list = []
for i in range(0, len(results)):
    results_list.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]) + '\n' + str(results[i][2]))
  
myResults = [list(x) for x in results]



# We can write the results in Pandas DataFrame
df = pd.DataFrame(columns=('Items','Antecedent','Consequent','Support','Confidence','Lift'))

Support =[]
Confidence = []
Lift = []
Items = []
Antecedent = []
Consequent=[]

for RelationRecord in results:
    for ordered_stat in RelationRecord.ordered_statistics:
        Support.append(RelationRecord.support)
        Items.append(RelationRecord.items)
        Antecedent.append(ordered_stat.items_base)
        Consequent.append(ordered_stat.items_add)
        Confidence.append(ordered_stat.confidence)
        Lift.append(ordered_stat.lift)

df['Items'] = list(map(set,Items))                                   
df['Antecedent'] = list(map(set,Antecedent))
df['Consequent'] = list(map(set,Consequent))
df['Support'] = Support
df['Confidence'] = Confidence
df['Lift']= Lift


df.sort_values(by='Lift', ascending=False, inplace=True)


