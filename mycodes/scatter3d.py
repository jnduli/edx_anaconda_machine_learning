# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:40:35 2016

@author: rookie
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mpl.style.use('ggplot')

student_dataset = pd.read_csv("students.data",index_col=0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Alcohol')
ax.scatter(student_dataset.G1, student_dataset.G3, student_dataset.Dalc, c='r', marker='.')
plt.show()
