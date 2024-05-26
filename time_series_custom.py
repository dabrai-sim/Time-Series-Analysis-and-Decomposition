import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load custom time series data
tsdata = np.loadtxt('tsdata.txt')
df = pd.DataFrame(tsdata, columns=['Timestamp', 'Variable'])

# Convert integer to datetime format
df.index = pd.to_datetime(df['Timestamp'], format="%Y%m%d")
df.drop('Timestamp', axis=1, inplace=True)

# Plot time series data
df['Variable'].plot(kind='line', color='red', title='Time Series Data')
plt.xlabel('Timestamp')
plt.ylabel('Variable')
plt.show()

# Plot a sample of 100 rows
df.iloc[:100, 0].plot(kind='line', color='red', title='Sample of 100 rows')
plt.xlabel('Timestamp')
plt.ylabel('Variable')
plt.show()

# Plot histogram of the variable
df['Variable'].plot(kind='hist', color='green', title='Histogram')
plt.xlabel('Variable')
plt.show()

# Perform differencing
df['10DF'] = df['Variable'].diff()
df['20DF'] = df['10DF'].diff()
df['30DF'] = df['20DF'].diff()

# Plot differenced data
plt.plot(df.index, df['Variable'], color='brown', label='Variable')
plt.plot(df.index, df['10DF'], color='blue', label='10DF')
# plt.plot(df.index, df['20DF'], color='red')
# plt.plot(df.index, df['30DF'], color='pink')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Variable')
plt.title('Differenced Data')
plt.show()
