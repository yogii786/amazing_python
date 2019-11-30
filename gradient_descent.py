import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



x= np.array([1,2,3,4,5])
y= np.array([5,7,9,11,13])  # y = x*w + b   where w = weights or slope and b = bias , x = input/features, y = output/labels

def gradient_descent(x,y):
    w_initial = b_initial = 0
    rate = 0.01
    n= len(x)
    plt.scatter(x,y)
    for i in range(100):
        y_predicted = w_initial*x + b_initial
        plt.plot(x, y_predicted , color = 'red')     # c = (1/n)*sum((y - y_predicted)**2)  this is known as cost function
        wd = -(2/n)*sum(x*(y-y_predicted))  # partial derivative of cost function with respect to weight w
        bd = -(2/n)*sum(y-y_predicted)      # partial derivative of cost function with respect to bias b
        w_initial = w_initial - rate * wd
        b_initial = b_initial - rate * bd
        
 gradient_descent(x,y)
