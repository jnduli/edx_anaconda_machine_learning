# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:29:44 2016

@author: rookie
"""

from sklearn.feature_extraction.text import CountVectorizer

corpus =["Authman ran faster than Harry because he is an athlete.",
         "Authman and Harry ran faster and faster.",]

bow = CountVectorizer()
X = bow.fit_transform(corpus)
print bow.get_feature_names()
print X.toarray()