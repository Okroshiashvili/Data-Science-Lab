"""
Created on Thu May 16 2019

@author: Nodar Okroshiashvili
""""




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



insurance_data = pd.read_csv('data/insurance.csv')



# Scatter Plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])



# Add regression line to the scatter plot.
# This is the best fit line to this data
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])



# We can use scatter plots to display the relationship between not two
# but three variables. This is done by coloring the plotted points
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'],
                hue=insurance_data['smoker'])



# Let add regression line
# But we know that we have three variable scatter plot and adding one
# regression line would not be correct. We can add two regression line
sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)



# We use scatter plot to represent relationship btw two constinuous variable
# Now let plot scatter plot for categorical variable
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])


