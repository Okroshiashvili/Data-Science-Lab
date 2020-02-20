


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data/fifa.csv', index_col='Date', parse_dates=True)

# Set the plot size in pixels
plt.figure(figsize=(10,6))
# Plot the line
sns.lineplot(data = df)
