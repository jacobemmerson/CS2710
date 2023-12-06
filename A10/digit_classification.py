#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:33:22 2023

@author: milos
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler  
from sklearn.model_selection import train_test_split

### ML Classification models
from sklearn.linear_model import LogisticRegression  # Log reg
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, confusion_matrix

# Load the digits dataset
digits = datasets.load_digits()

# Display the first digit
plt.figure(2, figsize=(3, 3))
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)
plt.show()

for comp in [[5,6],[1,7],[3,8],[0,8],[4,6],[6,8]]:
    print(f'\nNumbers = {comp}')
    # pick examples of digits 5 and 6 only
    index = [a for a in range(len(digits.target)) if digits.target[a] in comp]

    n_samples=len(index)
    data=digits.images[index].reshape((n_samples, -1))
    labels=digits.target[index]

    # divide the data to the train and test set
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, shuffle=False)

    # scale X components
    scaler = StandardScaler()
    scaler.fit(X_train)  
    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test)

    # initialize a LogReg model
    logreg = LogisticRegression()
    # train the Logreg model
    logreg.fit(X_train, y_train)

    ### Train datat
    print("***** Train data stats *****")
    prediction_LR = logreg.predict(X_train)
    # Test Accuracy
    print("Train score: {:.2f}".format(logreg.score(X_train, y_train)))
    #Test Confusion matrix
    conf_matrix = confusion_matrix(y_train, prediction_LR)
    print(conf_matrix)

    # make class prediction on test data 
    print("***** Test data stats *****")

    # make class prediction for the LogReg model
    prediction_LR = logreg.predict(X_test)

    # Test Accuracy
    print("Test score: {:.2f}".format(logreg.score(X_test, y_test)))

    #Test Confusion matrix
    conf_matrix = confusion_matrix(y_test, prediction_LR)
    print(conf_matrix)

