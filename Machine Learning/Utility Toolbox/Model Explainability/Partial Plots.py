


"""

While feature importance shows what variables most affect predictions,
partial dependence plots show how a feature affects predictions.


Like permutation importance, partial dependence plots are calculated after
a model has been fit.
The model is fit on real data that has not been artificially manipulated
in any way.

"""




"""
Data link:
    https://www.kaggle.com/mathan/fifa-2018-match-statistics#FIFA%202018%20Statistics.csv

"""






import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pdpbox import get_dataset, info_plots, pdp
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('FIFA 2018 Statistics.csv')


y = (df['Man of the Match'] == 'Yes')

feature_names = [i for i in df.columns if df[i].dtype in [np.int64]]


X = df[feature_names]


X_train, X_val, y_train, y_val = train_test_split(X,y, random_state=1)


tree_model = DecisionTreeClassifier(random_state=0, max_depth=5,
                                    min_samples_split=5).fit(X_train, y_train)



# Let visualize the tree

tree_graph = tree.export_graphviz(tree_model, out_file=None, feature_names=feature_names)

graphviz.Source(tree_graph)



"""

Partial Dependence Plot

"""


# Create data to plot
# Actually, this is one feature, in this case "Goal Scored"

pdp_goals = pdp.pdp_isolate(model= tree_model, dataset=X_val,
                            model_features=feature_names, feature='Goal Scored')



# Plot
pdp.pdp_plot(pdp_goals, 'Goal Scored')
plt.show()

"""
Let interpret the resulted plot:
    
The y axis is "change in the prediction" from what it would be
predicted at the baseline or leftmost value.

A blue shaded area indicates level of confidence.


From this graph we conclude that scoring a goal substantially increases
players chance of winning "Man of the Match". But extra goals beyond that
appear to have little impact on predictions.

"""


# Plot features in for loop

base_features = ['Goal Scored',
                 'Distance Covered (Kms)',
                 'Attempts',
                 'Free Kicks']


for feat_name in base_features:
    pdp_dist = pdp.pdp_isolate(model=tree_model, dataset=X_val,
                               model_features=base_features,feature=feat_name)
    pdp.pdp_plot(pdp_dist, feat_name)
    plt.show()

# This does not produce any plot because I choose 4 features, while model
# have 18 features and this for loop produced following error:
# "Number of features of the model must match the input. 
# Model n_features is 18 and input n_features is 4"
    
# It would be good to run this for loop in jupyter notebook and use all features




# Another example


feature_to_plot = 'Distance Covered (Kms)'

pdp_distance = pdp.pdp_isolate(model=tree_model, dataset=X_val,
                               model_features=feature_names, feature=feature_to_plot)

pdp.pdp_plot(pdp_distance,feature_to_plot)
plt.show()


"""
This plot almost exactly replicates Decision Tree structure.

Let train Random Forest and make same plot with Random Forest.

"""


rf_model = RandomForestClassifier(random_state=0).fit(X_train, y_train)


pdp_distanc = pdp.pdp_isolate(model=rf_model, dataset=X_val,
                               model_features=feature_names, feature=feature_to_plot)


pdp.pdp_plot(pdp_distanc, feature_to_plot)
plt.show()

"""
From this graph we can conclude that the model thinks that player are more likely
to win the "Man of the Match" if the whole team run a total of 100km over the
course of the game. Though running much more causes lower predictions.


Though this datset is small enough that we would be carefull in how
we interpret any model.

"""



###           2D Partial Dependence Plots         ###


"""
If we interested in interactions between features we need 2d partial dependece plot

"""

features_to_plot = ['Goal Scored', 'Distance Covered (Kms)'] 

inter1 = pdp.pdp_interact(model=tree_model, dataset=X_val,
                          model_features=feature_names,features=features_to_plot)

pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=features_to_plot,
                      plot_type='contour')
plt.show()


"""
This graph shows predictions for any combination of Goals Scored
and Distance covered.

we see the highest predictions when a team scores at least 1 goal
and they run a total distance close to 100km. 

If they score 0 goals, distance covered doesn't matter.

"""


