import pandas as pd
import matplotlib.pyplot as plt

# Load Yahoo stock data
dz = pd.read_csv('yahoo_stock.csv')

# Convert integer to datetime format
dz.index = pd.to_datetime(dz['Date'], format="%Y-%m-%d")

# Plot Adjusted Close price
dz['Adj Close'].plot(kind='line', color='red', title='Adjusted Close Price')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.show()

# Plot histogram of Adjusted Close price
dz['Adj Close'].plot(kind='hist', color='green', title='Histogram')
plt.xlabel('Adj Close')
plt.show()

# Plot box plot of Adjusted Close price
dz['Adj Close'].plot(kind='box', color='blue', title='Box Plot')
plt.ylabel('Adj Close')
plt.show()

# Perform differencing
dz['10DF'] = dz['Adj Close'].diff()
dz['20DF'] = dz['10DF'].diff()
dz['30DF'] = dz['20DF'].diff()

# Plot differenced data
plt.plot(dz.index, dz['Adj Close'], color='brown', label='Adj Close')
plt.plot(dz.index, dz['10DF'], color='blue', label='10DF')
# plt.plot(dz.index, dz['20DF'], color='red')
# plt.plot(dz.index, dz['30DF'], color='pink')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Adj Close')
plt.title('Differenced Data')
plt.show()
