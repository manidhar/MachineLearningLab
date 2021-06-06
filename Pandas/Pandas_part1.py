# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:21:10 2021

@author: Manidhar Karnatakam
"""

import pandas as pd

# reading the csv file from
df=pd.read_csv('players_data.csv')
df.head()
df.columns
df.info()
df.tail()
type(df)
df.to_csv('test.csv')
pd.read_csv('test.csv')

df1=pd.read_html('''https://www.basketball-reference.com/players/i/ibakase01.html?utm_source=direct&utm_medium=Share&utm_campaign=ShareTool''')
