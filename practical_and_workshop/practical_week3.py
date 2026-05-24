import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris(as_frame=True)
df = iris.frame.copy()
df["target"] = iris.target

print(df.shape)
print(df.columns.tolist()) # all the names of a column 
print(df.dtypes) # datatypes
print(df.head()) # show first 5 rows
print(df.describe(include='all'))
print(df["target"].value_counts().sort_index())
print(df.isna().sum())

X = df.drop(columns=["target"])     
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)