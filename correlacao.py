# -*- coding: utf-8 -*-
"""
@author: lucas
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Importa dados do Yahoo Finance
tickers = ["PG", "BEI.DE"]
data = wb.DataReader(tickers, data_source="yahoo", start="2010-1-1")["Adj Close"]
data.head()

# Calcula a taxa de retorno diaria das açoes
data_return = pd.DataFrame()
data_return["PG"] = (data["PG"] / data["PG"].shift(1)) - 1
data_return["BEI.DE"] = (data["BEI.DE"] / data["BEI.DE"].shift(1)) - 1

# Calcula a variancia anual das açoes
pg_var_a  = data_return["PG"].var() * 250
bei_var_a = data_return["BEI.DE"].var() * 250

# Calcula a matriz de covariancia das açoes
cov_matrix = data_return.cov()
cov_matrix
cov_matrix_a = data_return.cov() * 250
cov_matrix_a

corr_matrix = data_return.corr()
corr_matrix