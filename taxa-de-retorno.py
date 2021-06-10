# -*- coding: utf-8 -*-
"""
@author: lucas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

# Obtem dados da web, do yahoo finance
pg = wb.DataReader("PG", data_source="yahoo", start="1995-1-1")
pg.head()

# Faz o calculo da taxa de retorno simples dia a dia
pg["simple_return"] = (pg["Adj Close"] / pg["Adj Close"].shift(1)) - 1
pg["simple_return"]

# Plota o grafico da taxa de retorno diaria
pg["simple_return"].plot(figsize=(8, 5))
plt.show()

# Calcula a media da taxa de retorno diaria
# Calula a media da taxa de retorno multiplicada para tornar anual
# Mostra a porcentagem da taxa de retorno anual
avg_return_d = pg["simple_return"].mean()
avg_return_d 
avg_return_a = avg_return_d * 250
print("Taxa de Retorno anual: " + str(round(avg_return_a, 5)*100) + "%")