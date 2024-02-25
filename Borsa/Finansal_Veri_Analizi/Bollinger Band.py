import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from yahoofinancials import YahooFinancials
import plotly.graph_objects as go
from statsmodels.tsa.seasonal import seasonal_decompose

apple_df = yf.download('GOOGL', start = '2020-10-10', progress=False)
apple_df.index = pd.to_datetime(apple_df.index)

close_app = apple_df.iloc[(len(apple_df)//2):,3]
print(close_app.head())

rolling_app5 = close_app.rolling(window=5).mean()
rolling_app14 = close_app.rolling(window=14).mean()
rolling_app21 = close_app.rolling(window=21).mean()

MAs = pd.concat([close_app,rolling_app5,rolling_app14,rolling_app21], axis=1)
MAs.columns = ['Close', 'short', 'mid', 'long']
print(MAs.head(30))

MAs.dropna(axis=0, inplace=True)
print(MAs.head(5))

gorsel, ax = plt.subplots(figsize=(12,4))
ax.plot(close_app.index, close_app, label='Apple')
ax.plot(rolling_app5.index,rolling_app5, label='5 days rolling')
ax.plot(rolling_app14.index,rolling_app14, label='14 days rolling')
ax.plot(rolling_app21.index,rolling_app21, label='21 days rolling')
ax.legend(loc='upper left')

