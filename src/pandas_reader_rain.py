# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:12:54 2018

@author: apa
"""
import pandas as pd

fn = "../data/funabashi_rainfall.txt"
dataframe = pd.read_csv(fn,sep='\t', 
                        index_col=0,header=None
                        , names=['Rainfall (mm)'])
#dataframe.plot()
# Lets calculate annual maximum flow
dataframe.index = pd.to_datetime(dataframe.index)
annualm = dataframe.resample('A').sum()
monthlym = dataframe.resample('M').sum()
quartm = dataframe.resample('3M').sum()
ax=annualm.plot()
monthlym.plot(ax=ax)
quartm.plot(ax=ax)