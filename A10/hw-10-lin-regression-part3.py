#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:17:41 2022

@author: milos
"""

# Problem 2. Part 1. Linear regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 
from sklearn import datasets, linear_model, preprocessing
from sklearn.metrics import mean_squared_error

# load the boston housing dataset
housing = datasets.fetch_openml(name='boston',version=1,parser='auto')
housing.details 

X=housing.data
Y=housing.target

# train/test split
X_train=X[:-100]
X_test=X[-100:]
Y_train=Y[:-100]
Y_test=Y[-100:]

print(f"Train Input Dimensions: {X_train.shape}")
print(f"Test Input Dimensions: {X_test.shape}")

# scale X components
scaler = StandardScaler()
scaler.fit(X_train)  
X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)

# number of iterations for fitting w/ stochastic gradient descent
niter = 1000
tau = 0.05 # learning rate
n_samples = X_train.shape[0] # number of samples in training set
n_feats = X_train.shape[1] # number of features

# +1 for intercept
weights = np.ones(shape = n_feats + 1, dtype = np.float64)
for t in range(1,niter+1):
      # annealed rate
      rate = tau/t
      train_index = (t-1) % n_samples
      b = weights[0] # intercept
      w = weights[1:] # slope coef

      # sample
      x = X_train[train_index,:]
      y = Y_train[train_index]

      # single sample, use dot product
      gradient = y - (w.dot(x) + b)
      weights[0] = b + rate*gradient
      weights[1:] = w + rate*gradient*x

# Create linear regression object
regr = linear_model.LinearRegression()
regr.intercept_ = weights[0]
regr.coef_ = weights[1:]

# Print regression coefficients
print('Coefficients: \n', regr.coef_)
print('Intercept: \n', regr.intercept_)

Y_train_pred = regr.predict(X_train)
print(f"MSE on Training Set: {round(mean_squared_error(Y_train, Y_train_pred),2)}")


# Make predictions on the testing set
Y_test_pred = regr.predict(X_test)
# The mean squared error on the test set
print('Mean squared testing error: %.2f'
      % mean_squared_error(Y_test, Y_test_pred))


       
                    
