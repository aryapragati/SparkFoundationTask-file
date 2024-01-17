#!/usr/bin/env python
# coding: utf-8

# In[5]:



import pandas as pd
from sklearn.linear_model import LinearRegression

# Data
data = {
    'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8],
    'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 30, 54, 35, 76, 86]
}

df = pd.DataFrame(data)

# Model
model = LinearRegression()
model.fit(df[['Hours']], df['Scores'])

# Prediction
hours = 9.25
predicted_score = model.predict([[hours]])[0]

print(f"The predicted score for {hours} hours of study per day is: {predicted_score:.2f}")


