
# <----- Pipeline in Machine Learning worflow and steps ----->

# Step 1: Importing Libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split        # train to learn and test to check performance
from sklearn.linear_model import LogisticRegression     # importing a machine learning algorithm 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# Step 2: Loading Data

data = pd.read_csv("data.csv")      # read_csv is a function to read a csv file

print(data.head())      # shows first 5 rows
print(data.tail())      # last 5 rows
print(data.iloc[5:])    # deletes first 5 rows
print(data.iloc[:-5])   # it is same like array indexing can take start:end:step also


# Step 3: Cleaning Data

data = data.dropna()        # it will remove rows with missing values
                            # age	salary
                            # 25	50000
                            # NaN	60000 (this one)
                            # After dropna() → second row removed 
#print(data)                            

data['age'] = data['age'].fillna(data['age'].mean()) # data ['age'] select age column and illna means 
                                                    # it will remove the missing values with mean (average) age
# print(data['age'])                                                


# Step 4: Filtering Data

data = data[data['salary']>50000]
# print(data)

data = data[data['purchased']>0]
# print(data)


# Step 5: Features & Labels

x = data[['age', 'salary']].values      # x is the input feature 
y = data['purchased'].values            # y is the output label or target

print(x)                                # values converts pandas to numpy array
print(y)



# Step 6: Train-Test Split


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# train_test_split() → splits data
# test_size=0.2 → 20% test, 80% train
# random_state=42 → same result every time

# X_train → training input      "X" is a matrix (2d array) because it is in a table shape (heights, weights)
# X_test → testing input
# y_train → training output     "y" is a vector (1d array) the thing we are trying to predict (price)
# y_test → testing output



# Step 7: Model Training

model = LogisticRegression()        # reates an object
model.fit(X_train, y_train)      # the model will now learn about its pattern in the data 
                                # and fit() is a trainign process


# Step 8: Prediction

y_pred = model.predict(X_test)      # preidct(): model gives output and uses learned knowledge


# Step 9: Evaluation

print("Accuracy", accuracy_score(y_test, y_pred))

# accuracy score compares real_answers and predicted answers
# accuracy = correct predictions / total



# Step 10: Pipeline

pipeline = Pipeline([           # Pipeline = automatic workflow (scale data and train the model)
    ('scaler', StandardScaler()),       # standard scaler normises the data (to understand better) 
    ('model', LogisticRegression())
])

pipeline.fit(X_train, y_train)      # runs all steps automatically



# save the model
import joblib
joblib.dump(pipeline, "model.pkl")

model = joblib.load("model.pkl")


