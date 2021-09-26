# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:50:42 2020

@author: KRISHNA
"""
import string
import numpy as np
from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import classification_report
import filefetch
import radar
import pickle

name=input("Enter name:")
datname=str(name)
testset=filefetch.fetch(name)
print(len(testset))

with open("model.pkl",'rb') as fin:
    features,clf=pickle.load(fin)
    
X_test_dataset = np.zeros((len(testset),len(features)))
for i in range(len(testset)):
    #print(i) # Uncomment to see progress
    abcd=testset[i][1]
    eee=""
    for j in abcd:
        eee=eee+" "+j
    word_list = [ word.strip(string.punctuation).lower() for word in eee.split()]
    for word in word_list:
        if word in features:
            X_test_dataset[i][features.index(word)] += 1

Ypred=clf.predict(X_test_dataset)
an,goal=np.unique(Ypred, return_counts=True)
print(an)
print(goal)
radar.graphgen(datname,goal)