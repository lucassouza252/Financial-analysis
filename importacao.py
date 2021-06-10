# -*- coding: utf-8 -*-
"""
Importaçao e Organização de Dados
@author: lucas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

ser = pd.Series(np.random.random(5), name="column 01")
ser

PG = wb.DataReader("PG", data_source="yahoo", start="1995-1-1")
PG.head()
PG.tail()
PG.info()

tickers = ["PG", "MSFT", "T", "F", "GE"]
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source="yahoo", start="1995-1-1")["Adj Close"]

new_data.head()
new_data.info()

oibr = wb.DataReader("OIBR3.SA", data_source="yahoo", start="2015-1-1")
oibr.head()
plt.plot(oibr["Close"])
plt.plot(oibr["Open"])
plt.show()