# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

ordered_satisfaction = ['Very Unhappy','Unhappy','Neutral','Happy', 'Very Happy']
df= pd.DataFrame({'satisfaction':['Mad','Happy','Unhappy','Neutral']})
df.satisfaction = df.satisfaction.astype("category",
                                         ordered=True,
                                         categories=ordered_satisfaction).cat.codes
print df

dt = pd.DataFrame({'vertebrates': ['Bird',
                                   'Bird',
                                   'Mammal',
                                   'Fish',
                                   'Amphibian',
                                   'Reptile',
                                   'Mammal']})
#dt['vertebrates'] = dt.vertebrates.astype("category").cat.codes

#print dt

dt =pd.get_dummies(dt,columns=['vertebrates'])
print dt