import numpy as np
import time

import scipy
from scipy.spatial.distance import cdist

x = np.random.rand(1000)
y = np.random.rand(1000)
ans = x**2 + y**2
# print(ans)


arr = np.array([[1,2,3], [4,5,6]])
row_sum = np.sum(arr, axis=1, keepdims=True)       # row wise normalisation
norm = arr/row_sum
print(norm)     # each rows sum to 1

column_sum = np.sum(arr, axis=0, keepdims=True)
norm = arr/column_sum
print(norm)



rand_matrix = np.random.randint(0, 1000, (4,5))
print(rand_matrix)

mean_of_column = np.mean(rand_matrix, axis=0)
sub = rand_matrix - mean_of_column
print(sub)

# multiple two arrays 
arr1 = np.random.randint(1, 10, (2,3))
arr2 = np.random.randint(1, 10, (2,3))

# element wise multiplication
print(arr1 * arr2)                  # both are same bro
print(np.multiply(arr1, arr2))

# matrix multiplication and for this we have to change the shape it can't be (2,3) both one has to be 
# (3,2) = (2,2) to get output.

arr3 = np.random.randint(1, 10, (3,2))
# print(arr1 @ arr3)                # they are all same
# print(np.dot(arr1, arr3))
# print(arr1.dot(arr3))

# dot product

arr4 = np.array([[1,2], [4,5]])
arr5 = np.array([[7,8], [10,11]])

print(np.dot(arr4, arr5))      # dot product means [1*]
print(np.inner(arr4, arr5))
print(np.matmul(arr4, arr5))    # same to dot but can be used for batch multiplication and higher dimension



a = np.random.randint(100, size=(5,3))
b = np.arange(3)
print(a.dot(b))

# vector distances and length (norm) of a vector
u = np.array([1,2,3])
v = np.array([4,5,6,])

# vector difference
diff = u-v

# eucledian distance 
# interesting facxt is that numpy is doing all of these calculations here

# Subtract vectors: u - v = [-3, 2, 0]
# Square each element: [-3^2, 2^2, 0^2] = [9, 4, 0]
# Sum squares: 9 + 4 + 0 = 13
# Take sqrt: √13 ≈ 3.605

dist = np.linalg.norm(diff)
print(dist)

c = np.array([[1,2,3], [4,5,6]])
d = np.arrat([[7,8,9], [10,11,12]])

distances = cdist(c, d, metric = 'euclidean')
distances1 = cdist(c, d, metric = 'cityblock')  # manhattan distance
distances2 = cdist(c, d, metric = 'cosine')

print(distances)
print(distances1)
print(distances2)




# <----- Linear regression ----->
def linear_regression_predict(w: np.ndarray, x: np.ndarray, b: float) -> float:
    y = np.dot(w,x) + b             # Prediction = (weights × inputs) + bias
    return y


# <----- Mean squared error ----->
def mse_loss(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    error = y_pred - y_true
    squared_error = error**2
    mse = np.mean(squared_error)
    return mse


