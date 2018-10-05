# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:56:33 2018

@author: apa
"""

from matplotlib import pyplot as plt
import pandas as pd


df=pd.read_csv("https://datahub.io/core/gdp/r/gdp.csv")
ax=plt.gca()
for country in ['Nepal', 'Paraguay','Sri Lanka']:
    df1=df.loc[df['Country Name']==country]
    df1.plot(x='Year', y='Value', label=country, ax=ax)
plt.show()