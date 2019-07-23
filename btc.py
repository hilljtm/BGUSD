# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('ggplot')


# import csv
df = pd.read_csv('BTCUSD.csv')

# drop columns not needed and store in new DF
df = df.drop(['Adj_Close'], axis=1)
df = df.drop(['Volume'], axis=1)


# plot a lineplot using our DF
fig, ax = plt.subplots()
ax.plot('Date', 'Close', data=df)
plt.xticks('Date', rotation='vertical')

fig.autofmt_xdate()
ax.fmt_xdata = mdates.DateFormatter('%m-%d')


# x-axis


ax.set(xlabel='Date (2019)', ylabel='Price (USD)',
       title='Bitcoin so far in 2019')

ax.grid(True)
fig.tight_layout()
fig.autofmt_xdate()
plt.show()


# %%
