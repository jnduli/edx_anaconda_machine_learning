# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:40:35 2016

@author: rookie
"""

import pandas as pd
import matplotlib as mpl

mpl.style.use('ggplot')

student_dataset = pd.read_csv("students.data",index_col=0)
student_dataset.plot.scatter(x='G1', y='G3')
