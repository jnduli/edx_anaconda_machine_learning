# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:52:16 2016

@author: rookie
"""

import pandas as pd
import matplotlib as mpl

mpl.style.use('ggplot')

student_dataset = pd.read_csv("students.data",index_col=0)
my_series =student_dataset.G3
my_dataframe = student_dataset[['G3','G2','G1']]

#my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5, normed=False)
