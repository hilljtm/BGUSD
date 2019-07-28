# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('ggplot')

# import csv
df = pd.read_csv('USDindex.csv')

# turn date column to type datetime, and set it as index
df.Date = pd.to_datetime(df.Date)
df.set_index('Date', inplace=True)

# drop columns not needed, note: you can do this in one line
df = df.drop(['Vol'], axis=1)
df = df.drop(['Change'], axis=1)
df = df.drop(['Low'], axis=1)
df = df.drop(['High'], axis=1)
df = df.drop(['Open'], axis=1)

# plot using pandas built-in method
df.plot(figsize=(20, 10), linewidth=3, fontsize=20)
plt.xlabel('Month', fontsize=20)

# %%
# identify trends in time series by taking the rolling average
price = df[['Price']]
price.rolling(7).mean().plot(figsize=(20, 10), linewidth=3, fontsize=20)
plt.xlabel('Month', fontsize=20)
