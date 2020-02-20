


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


flight_data = pd.read_csv('data/flight_delays.csv',index_col='Month')



# Bar chart
plt.figure(figsize=(10,6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

sns.barplot(x=flight_data.index, y=flight_data['NK'])

plt.ylabel('Arrival delay (in minutes)')
plt.show()


# Heatmap
plt.figure(figsize=(10,6))
plt.title("Average Arrival Delay for Each Airline, by Month")

sns.heatmap(data=flight_data, annot=True)

plt.xlabel('Airline')
plt.show()


