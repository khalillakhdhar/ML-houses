# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:44:45 2023

@author: khali
"""
import pandas as pd
from sklearn.linear_model import LinearRegression

#step1 
data =pd.read_csv("houses.csv")
#print(data)

X=data[["bedrooms","bathrooms","sq_ft"]]
y=data["price"]
#print(X)
#step2
model =LinearRegression() 
model.fit(X,y)
new_house=[[3,2,2000]]
price_pred=model.predict(new_house)
print("the predicted price is",price_pred[0])
