# Task 4.1 - Use linear regression on diabetes dataset
# Somehow this code doesn't run on a conventional Python file so here we are
# 4.1.1 contains the whole code (copy it out)
# 4.1.2 contains the code as a whole in .ipynb

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split

diabetes=datasets.load_diabetes()
# print(diabetes.data.shape)
# print(diabetes.target.shape)
# print(diabetes.target)
# print(diabetes.feature_names)

# test_size=0.2 means that 20% of the data will be used for testing
x_train,x_test,y_train,y_test=train_test_split(diabetes.data,diabetes.target,test_size=0.2,random_state=0)
# print(x_train.shape)
# print(x_test.shape)

model=LinearRegression()
model.fit(x_train,y_train)

model.score(x_test,y_test) # using test data to check how accurate it is