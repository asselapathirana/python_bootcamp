# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:12:54 2018

@author: apa
"""
import pandas as pd

fn = "../data/mean-daily-flow-cumecs-jokulsa-e.tsv"
dataframe = pd.read_csv(fn,sep='\t', index_col=0)
#dataframe.plot()
# Lets calculate annual maximum flow
dataframe.index = pd.to_datetime(dataframe.index)
annualm = dataframe.resample('A').mean()
annualm.plot()