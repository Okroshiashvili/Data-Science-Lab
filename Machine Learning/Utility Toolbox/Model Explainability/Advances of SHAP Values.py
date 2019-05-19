"""
Created on Sun May 19 2019

@author: Nodar Okroshiashvili
"""





"""
Here we investigate how aggregating many SHAP values can give more detailed
alternatives to permutation importance and partial dependence plots.


Shap values show how much a given feature changed our prediction
(compared to if we made that prediction at some baseline value of that feature).


"""



"""
Data link:
    https://www.kaggle.com/mathan/fifa-2018-match-statistics#FIFA%202018%20Statistics.csv

"""






import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('FIFA 2018 Statistics.csv')

y = (data['Man of the Match'] == "Yes")

feature_names = [i for i in data.columns if data[i].dtype in [np.int64, np.int64]]

X = data[feature_names]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

my_model = RandomForestClassifier(random_state=0).fit(train_X, train_y)




# We get the SHAP values for all validation data with the following code.


import shap

# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)


# Calculate shap_values for all of val_X rather than a single row,
# to have more data for plot.
shap_values = explainer.shap_values(val_X)


# Make plot
shap.summary_plot(shap_values[1], val_X)



"""
This plot gives all the features contribution to the model.
what if we want to delve into single feature?

Here comes SHAP dependence contribution plot.



Partial Dependence Plots show how single feature impacts predictions.
But PDP does not show what's the distribution of effect

"""




shap_values = explainer.shap_values(X)


shap.dependence_plot('Ball Possession %', shap_values[1], X,
                     interaction_index="Goal Scored")




"""
In the plot, x axis represents actual feature, in this case "Ball Possession %"
and y axis represents SHAP values corresponding to actual ball possession values.

The fact this slopes upward says that the more you possess the ball,
the higher the model's prediction is for winning the Man of the Match award.


The spread suggests that other features must interact with Ball Possession %.

"""





