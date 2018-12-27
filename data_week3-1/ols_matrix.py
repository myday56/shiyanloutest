import pandas as pd
#from numpy import *
import numpy as np
def w_matrix(x,y):
    w = (x.T * x).I * x.T * y
    return w
def caculate_w():
    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    x = df['Brooklyn Bridge']
    y = df['Manhattan Bridge']
    
    a = np.ones(30,dtype=int)
    x = np.mat(np.column_stack((a,x)))
    y = np.mat(y)


    w = round(w_matrix(x,y.reshape(30,1)).tolist()[1][0],2)
    b = round(w_matrix(x,y.reshape(30,1)).tolist()[0][0],2)
    return w,b
print(caculate_w())
