# Lesson 4 - Cubic model applied on to a sine function
# Using linear regression to fit a cubic model on to a sine wave
# Somehow this code doesn't run on a conventional Python file so here we are
# 4.1 contains the whole code (copy it out)
# 4.2.1 contains code separated by parts
# 4.2.2 contains the code as a whole

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

x_axis=np.linspace(-np.pi,np.pi,1000)
# print(x_axis)
y_axis=np.sin(x_axis)
# print(y_axis)
# plt.plot(x_axis,y_axis) # apparently only works in .ipynb

features=np.array([
    x_axis,
    x_axis**2,
    x_axis**3
]).transpose() # inverts columns and rows
labels=y_axis
# now attempt to fit features against labels

model=linear_model.LinearRegression()
model.fit(features,labels)
# print(model.coef_)
model_out=np.array(model.coef_[0]*x_axis + model.coef_[1]*x_axis**2 + model.coef_[2]*x_axis**3)

plt.plot(x_axis,model_out,label="Model")
plt.plot(x_axis,y_axis,label="Sine")