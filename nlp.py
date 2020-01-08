# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:20:42 2020

@author: post
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter="\t", quoting = 3)
print(dataset)