# 1. Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Logging function
def log_step(step):
    print(f"[LOG]: {step}")

# 2. Create DataFrame
log_step("Creating dataset")

data = pd.DataFrame({
    'height': [170, 165, np.nan, 180, 175],
    'weight': [70, np.nan, 65, 80, np.nan],
    'gender': ['M', 'F', 'F', 'M', 'M'],
    'active': [1, 0, 1, 1, 0]
})

print(data)

# 3. Fill missing values
log_step("Filling missing values with mean")

data['height'] = data['height'].fillna(data['height'].mean())
data['weight'] = data['weight'].fillna(data['weight'].mean())

# 4. Encode gender
log_step("Encoding gender")

data['gender'] = data['gender'].map({'M': 0, 'F': 1})

# 5. Features and target
X = data[['height', 'weight', 'gender']]
y = data['active']

# 6. Pipeline (scaling + model)
log_step("Creating pipeline")

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# 7. Train model
log_step("Training model")

pipeline.fit(X, y)

# 8. Predictions
log_step("Making predictions")

predictions = pipeline.predict(X)
print("Predictions:", predictions)

# 9. Plot histogram
log_step("Plotting histogram")

plt.hist(data['weight'])
plt.title("Weight Distribution")
plt.xlabel("Weight")
plt.ylabel("Frequency")
plt.show()




# look for google collab notes for praxxtical task