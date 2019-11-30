import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



x= np.array([1,2,3,4,5])
y= np.array([5,7,9,11,13])

def gradient_descent(x,y):
    a_initial = b_initial = 0
    rate = 0.01
    n= len(x)
    plt.scatter(x,y)
    for i in range(100):
        y_predicted = a_initial*x + b_initial
        plt.plot(x, y_predicted , color = 'red')
        md = -(2/n)*sum(x*(y-y_predicted))
        yd = -(2/n)*sum(y-y_predicted)
        a_initial = a_initial - rate * md
        b_initial = b_initial - rate * yd
        
 gradient_descent(x,y)
