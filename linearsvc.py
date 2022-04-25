# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:08:23 2022

@author: hmdebern
"""
from imblearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.utils import resample


_pipeline = make_pipeline(MinMaxScaler(),LinearSVC())

x=np.zeros((100,5))
y= list(np.zeros((50,1))+np.zeros((50,1))

# self.classifier = self._pipeline
param_grid = {'linearsvc__C':np.arange(0.01,100,10)}
search = GridSearchCV(_pipeline, param_grid=param_grid)
search.fit(x,y)

X_undersampled, y_undersampled = resample(x[y == 1], y[y == 1],
                replace=True,
                n_samples=x[y == 0].shape[0],
                random_state=123)

classifier=search.best_estimator_
classifier.fit(x,y)
       