


"""

What if you want to break down how the model works for an individual prediction?

SHAP Values (an acronym from SHapley Additive exPlanations) break down
a prediction to show the impact of each feature.


SHAP values interpret the impact of having a certain value for a given feature
in comparison to the prediction we'd make if that feature took some baseline value.


Here we ask the following question:
    How much was a prediction driven by the fact that the team scored 3 goals,
    instead of some baseline number of goals.
    
If we answer this question for "number of goals", we could repeat the process
for all other features.



We decompose a prediction with the following equation:
    ```sum(SHAP values for all features) = pred_for_team - pred_for_baseline_values```


That is, the SHAP values of all features sum up to explain why
my prediction was different from the baseline.


"""






"""
Data link:
    https://www.kaggle.com/mathan/fifa-2018-match-statistics#FIFA%202018%20Statistics.csv

"""



import numpy as np
import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('FIFA 2018 Statistics.csv')


y = (df['Man of the Match'] == 'Yes')

feature_names = [i for i in df.columns if df[i].dtype in [np.int64]]


X = df[feature_names]


X_train, X_val, y_train, y_val = train_test_split(X,y, random_state=1)


my_model = RandomForestClassifier(random_state=0).fit(X_train, y_train)




# SHAP values

row_to_show = 5

# I use one row of data. Could be used multiple rows if desired
data_for_prediction = X_val.iloc[row_to_show]


data_for_prediction_array = data_for_prediction.values.reshape(1,-1)


my_model.predict_proba(data_for_prediction_array)



# The team is 70% likely to have a player win the award.

# Now, we'll move onto the code to get SHAP values for that single prediction.



# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)

# Calculate shap values

shap_values = explainer.shap_values(data_for_prediction)


"""
The "shap_values" object above is a list with two arrays.
The first array is the SHAP values for a negative outcome (don't win the award),
and the second array is the list of SHAP values for the positive outcome
(wins the award). We typically think about predictions
in terms of the prediction of a positive outcome,
so we'll pull out SHAP values for positive outcomes (pulling out shap_values[1]).

"""

shap.initjs()

shap.force_plot(explainer.expected_value[1], shap_values[1], data_for_prediction)



# Function to plot SHAP values

sample_data_for_prediction = X_val.iloc[0].astype(float)


def plot_shap(model, prediction_data):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(prediction_data)
    shap.initjs()
    return shap.force_plot(explainer.expected_value[1], shap_values[1], prediction_data)


