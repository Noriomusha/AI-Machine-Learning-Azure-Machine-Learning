# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:02:35 2022

@author: Edward Alvarado
"""

import pandas as pd
df =pd.read_csv('players.csv')

df.isnull().sum
print (df)
print()
print(" Data from the Esports Records ")

print(df)
