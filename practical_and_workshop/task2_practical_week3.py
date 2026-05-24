import pandas as pd
from sklearn import load_breast_cancer, pipeline
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = load_breast_cancer(as_frame=True)
df = data.frame.copy()
df["target"] = data.target 

X = df.drop(columns=["target"])
y = df["target"]

print(X)
pipeline = pipeline.Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(), 'clf', 'accuracy', 'f1', SVC(C=1.0, kernel='linear', random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
pipeline.fit(X_train, y_train)
print(pipeline.score(X_test, y_test))




