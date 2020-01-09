# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:20:42 2020

@author: post
"""
# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter="\t", quoting = 3)
#print(dataset)

# Cleaning the text
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
nltk.download('stopwords') # not relevant words
corpus = []
for i in range(dataset.shape[0]):
    
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i]) # Replace all eliminated chars with ' '
    #print(review) # return Wow    Loved this place
    review = review.lower() # to lower case
    review = review.split() # list of words
    ps = PorterStemmer() # Stemming (Racinisation l'origine du mot loved -> love)
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))] #set to speed up the algo
    review = ' '.join(review)
    #print(review)
    corpus.append(review)

# Creating the bag of words model
# sparce matrix of words included in the reviews ( columns : words, rows : reviews )
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
cv = CountVectorizer(max_features=1500) # only 1500 words
X = cv.fit_transform(corpus).toarray()
print(X)

y = dataset.iloc[:,1].values
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Random Forest Classifier to the training set
from sklearn impo