# Trend İndikatörü
# MACD - Hareketli ortalama (5, 14 ve 21 güne göre)
# Fiyat hareketlerinin farklı periyotlar için hareketli ortalaması trendin yönü hakkında bilgi vericidir.

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
#ax.savefig('hareketli_ortalama.png', dpi=150)

np.abs(np.percentile(np.array(MAs["short"] - MAs["mid"]),10))

def buy_sell(data, perc = 50):
    buy_sel = []
    buy_signal = []
    sell_signal = []
    flag = 42

    sm = np.abs(np.percentile(np.array(data["short"] - data["mid"]),perc))
    sl = np.abs(np.percentile(np.array(data["short"] - data["long"]),perc))

    for i in range(0,len(data)):
        if (data["short"][i] > data["mid"][i]+sm) & (data["short"][i] > data["long"][i]+sl):
            buy_signal.append(np.nan)
            if flag != 1:
                sell_signal.append(data["Close"][i])
                buy_sel.append(data["Close"][i])
                flag = 1
            else:
                sell_signal.append(np.nan)
        elif (data["short"][i] < data["mid"][i]-sm) & (data["short"][i] < data["long"][i]-sl):
            sell_signal.append(np.nan)
            if flag != 0:
                buy_signal.append(data["Close"][i])
                buy_sel.append(-data["Close"][i])
                flag = 0
            else:
                buy_signal.append(np.nan)
        else:
            buy_sel.append(np.nan)
            sell_signal.append(np.nan)
            buy_signal.append(np.nan)
    
    operations = np.array(buy_sel)
    operations = operations[~np.isnan(operations)]

    neg = 0
    pos = 0

    for i in range(len(operations)):
        if operations[i] < 0:
            neg = i
            break
    for i in range(1, len(operations)):
        if operations[-i] > 0:
            pos = i-1
            break
    operations = operations[neg:-pos]
    PL = np.sum(operations)

    return (buy_signal, sell_signal, PL)

m = buy_sell(MAs)
MAs["BUY"] = m[0]
MAs["SELL"] = m[1]

print(MAs)

plt.figure(figsize=(10,5))
plt.scatter(MAs.index, MAs["BUY"], color = "green", label = "BUY", marker='^', alpha=1)
plt.scatter(MAs.index, MAs["SELL"], color = "red", label = "SELL", marker='v', alpha=1)
plt.plot(MAs["Close"], label = "Close Price", alpha = 0.5)
plt.title("Close Price Buy and Sell Signals")
plt.xlabel("Date")
plt.ylabel("Clos Price")
plt.legend(loc = "upper left")
plt.show()
