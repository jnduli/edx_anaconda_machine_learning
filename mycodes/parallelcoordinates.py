# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:31:38 2016

@author: rookie
"""

from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates, andrews_curves

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')
# If the above line throws an error, use plt.style.use('ggplot') instead

# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names) 

print df
df['target_names'] = [data.target_names[i] for i in data.target]

# Parallel Coordinates Start Here:
plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()

plt.figure()
andrews_curves(df, 'target_names')
plt.show()