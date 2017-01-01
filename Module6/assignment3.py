import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap

def test_PCA(df, y):
    best_score = 0
    for i in range(4,15):
        pca = PCA(n_components = i)
        pca.fit(df)
        d = pca.transform(df)
        score = get_best_score(d, y)
        if score>best_score:
            best_score=score
    return best_score
def test_Isomap(df,y):
    best_score =0
    for i in range(2,6):
        for j in range(4,7):
            iso = Isomap(n_neighbors=i, n_components=j)
            iso.fit(df)
            d = iso.transform(df)
            score= get_best_score(d,y)
            if score>best_score:
                best_score = score
    return best_score

def test_pca_isomap(df,y):
    pca = test_PCA(df, y)
    iso = test_Isomap(df, y)
    if pca>iso:
        return pca
    else:
        return iso

def get_best_score(X,y):
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)
   best_score =0
   for i in np.arange(0.05, 2.05, 0.05):
        for j in np.arange(0.001, 0.101, 0.001):
            svc = SVC(C=i, gamma=j)
            svc.fit(X_train, y_train)
            score = svc.score(X_test, y_test)
            #aprint score
            if score > best_score:
                best_score = score
   return best_score 

X = pd.read_csv('Datasets/parkinsons.data')
y = X['status'].copy()
X.drop(labels=['name','status'], axis=1, inplace=True)

from sklearn.cross_validation import train_test_split
df = X
T= preprocessing.StandardScaler().fit_transform(df)
print "Standard Scaler :" , test_pca_isomap(T,y)
#jT= preprocessing.MinMaxScaler().fit_transform(df)
#print "Min Max Scaler ", get_best_score(T,y)
#T = preprocessing.MaxAbsScaler().fit_transform(df)
#print "Max abs scaler :", get_best_score(T,y)
#T = preprocessing.Normalizer().fit_transform(df)
#print "Normalizer :", get_best_score(T,y)

