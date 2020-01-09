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
nltk.download('stopwords') # not relevant words

review = re.sub('[^a-zA-Z]',' ',dataset['Review'][0]) # Replace all eliminated chars with ' '
print(review) # return Wow    Loved this place
review = review.lower() # to lower case
review = review.split() # list of words
review = [word for word in review if not word in set(stopwords.words('english'))] #set to speed up the algo

print(review) # ['wow', 'loved', 'place']
