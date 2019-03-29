""" Created in Mar 2019 by Paul A. Gureghian """

""" Create data visualization with data collected from Google Trends """

### Import packages
import pandas as pd 
import matplotlib.pyplot as plt

### Download data and create a Pandas dataframe
#https://trends.google.com/trends/explore?date=all&geo=US&q=Pancakes
pancake_data = pd.read_csv('/pancakes.csv', skiprows=2, parse_dates=['Month'], index_col=['Month']) 
print(pancake_data.head()) 
plt.plot(pancake_data) 

### Visualize the trend
y_mean = pancake_data.rolling('365D').mean()
plt.plot(y_mean)

### Highlight the Standard Deviation variance
y_std = pancake_data.rolling('365D').std()
plt.plot(y_mean)
plt.fill_between(y_mean.index, (y_mean - y_std).values.T[0], (y_mean + y_std).values.T[0], alpha = .5)

