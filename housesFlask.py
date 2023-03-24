# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:31:38 2023

@author: khali
"""

from flask import Flask, jsonify, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Step 1: Load the data and prepare the model
data = pd.read_csv("houses.csv")
X = data[["bedrooms", "bathrooms", "sq_ft"]]
y = data["price"]
model = LinearRegression()
model.fit(X, y)

# Step 2: Define the API endpoints
@app.route('/predict', methods=['POST'])
def predict_price():
    # Extract the data from the POST request
    data = request.get_json()
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    sq_ft = data['sq_ft']
    
    # Use the model to predict the price
    new_house = [[bedrooms, bathrooms, sq_ft]]
    price_pred = model.predict(new_house)[0]
    
    # Return the prediction as a JSON response
    return jsonify({'predicted_price': price_pred})

if __name__ == '__main__':
    app.run(debug=True)
