# -*- coding: utf-8 -*-
"""
@author: lucas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

# Carteira hipotetica com 4 açoes
tickers = ["PG", "F", "MSFT", "GE"]
mydata = pd.DataFrame()

# Obtem dados do Yahoo finance das 4 ações da carteira
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source="yahoo", start="1995-1-1")["Adj Close"]

mydata.head()
mydata.info()
mydata.iloc[0]

# Plota grafico com dados normalizado pela formula (p1/p0 * 100)
# Sem a normalização cada linha do grafico começaria em um ponto diferente
# O que dificulta a visualização dos dados
((mydata / mydata.iloc[0]) * 100).plot(figsize=(15, 6));
plt.show()

# Calculo de retornos das açoes em uma carteira com peso por açao
returns = (mydata / mydata.shift(1)) - 1
weights = np.array([0.25, 0.25, 0.25, 0.25])
annual_returns = returns.mean() * 250
portfolio_return = np.dot(annual_returns, weights)

print("Taxa de Retorno anual da carteira: " + str(round(portfolio_return, 5)*100) + "%")

