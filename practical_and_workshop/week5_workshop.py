# # # activity 1 computations

# # import time
# # import tracemalloc
# # import numpy as np

# # data = list(range(1_000_000))
# # tracemalloc.start()
# # start = time.time()


# # squares=[]
# # for x in data:
# #     squares.append(x**2)

# # total=sum(squares)
# # end=time.time()
# # print(end-start)

# import time
# import tracemalloc

# # ---------- 1. Python loops ----------
# data = list(range(1_000_000))

# tracemalloc.start()
# start = time.time()

# squares = []
# for x in data:
#     squares.append(x ** 2)
# total = sum(squares)

# end = time.time()
# current1, peak1 = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# print("Loop total:", total)
# print("Time (loop):", round(end - start, 4), "seconds")
# print("Memory (loop):", round(peak1 / 1024 / 1024, 4), "MB (peak)")
# print("\n" + "="*50 + "\n")

# # ---------- 2. NumPy Vectorised Operations ----------
import numpy as np
data_np = np.arange(1_000_000)

# tracemalloc.start()
# start = time.time()

# squares_np = data_np ** 2
# total_np = squares_np.sum()

# end = time.time()
# current2, peak2 = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# print("Vectorized total:", total_np)
# print("Time (vectorized):", round(end - start, 4), "seconds")
# print("Memory (vectorized):", round(peak2 / 1024 / 1024, 4), "MB (peak)")


# # numpy is repeating computation and cpu code

# my_list=[1,2,3,4,5]
# my_list+5 # gives error

# my_list=np.array[1,2,3,4,5]
# my_list+5 # will give output


# # element-wise operstiona nd chaining

# x=np.linspace(0,2*np.pi, 1000000)
# y=np.sin(x)+np.cos(x)
# z=np.exp(y)+np.log1p(y)

# print(z[:5])


# # broadcasting with different shapes

# arr1=np.arrange(6).resshape(2,3)
# arr2=np.array([11,22,33])

# arr1+arr2


# # practice:
# # compute(x**2 + y**2) for two arrays x and y of shape(1000, ) and primt their mean


# x=np.random(1000)
# y=np.random(1000)
# z=(x**2 + y**2)

# print(np.mean(z))
# # wec an also use this but not recommended 
# print(z.mean())




# # activity 2 : axis wise computation

# mat = np.array([[1,2,3], [4,5,6]])
# print(np.sum(mat,axis=0))   # column wise sum
# print(np.sum(mat,axis=1))   # row wise sum

# # try for mean function


##  normalisation

# mat = np.array([
#     [1,2,3], 
#     [4,5,6]
#     ])

# row_sum = np.sum(mat,axis=0)
# norm_mat = mat/row_sum[:, np.newaxis]
# norm_mat                # should be added to 1


# # min or max across axes

# mat.max(axis=0)     # column
# mat.max(axis=1)     # row

# mat.argmax(axis=1)
# np.cumsum(mat, axis=1) # in column commulative sum
# np.cumsum(mat, axis=0) # for rows

# # practice problem


# # create a 4*5 random integer matrix 
mat = np.random.randint(1, 100, size=(4,5))

# # # create mean of each column 
# col_means=np.means(mat,axis=0)

# # # subtract it from each column (normalized columns)
# norm_mat=mat-col_means

# norm_mat
# mat



# activity 3 : matrix multplication

# common shaoe transformations

# reshape  # reshape target dimensions
mat.reshape(10,2)

# ravel # flattens an existing matrix (1 d vector)
mat.ravel()

# transpose a matrix 
mat.T

# expand adds new dimensions 
new_mat = np.expand_dims(mat, axis=0)
np.expand_dims(mat, axis=1)
np.expand_dims(mat, axis=0).shape()
np.expand_dims(mat, axis=1).shape()

np.squeeze(new_mat) # remopves any dimensions of size 1


# matrix multiplication

import numpy as np

# Define two 2D arrays (matrices)
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# ----------------------------
# 1. Element-wise Multiplication
# ----------------------------
elementwise = A * B  # or np.multiply(A, B)

# ----------------------------
# 2. Matrix Multiplication
# ----------------------------
matmul_1 = A @ B      # Python 3.5+ syntax
matmul_2 = np.dot(A, B)  # equivalent
matmul_3 = A.dot(B)   # method syntax

# ----------------------------
# 3. Print Results
# ----------------------------
print("A:\n", A)
print("B:\n", B)
print("\nElement-wise Multiplication (A * B):\n", elementwise)
print("\nMatrix Multiplication (A @ B):\n", matmul_1)




# Multiply a (3, 4) matrix by a (4, 2) matrix and print the result.

a=np.random.randint(1,10, size=(3,4))
b=np.random.randint(1,10, size=(4,2))

print(a@b) 

# batch multiplication

batch_a=np.random.randint(1,10, size=(3,4,4))
batch_b=np.random.randint(1,10, size=(3,4,4)) # 4 rows, 4 columns (matrix ka matrix)

batch_matmul=np.matmul(batch_a, batch_b)
print(batch_matmul, batch_matmul.shape)


# activity 4 : dot product and inner product


x=np.array([[1,2], [5,6]])
y=np.array([[4,5], [4,3]])

print('Dot Product', np.dot(x,y))
print('Inner Product', np.inner(x,y))


# inner vs matmul product

x=np.array([[1,2], [5,6]])
y=np.array([[4,5], [4,3]])

print('Matmul Product:\n', np.matmul(x,y))
print('Inner Product:\n', np.inner(x,y))


# distance computation
a=np.array([0,2,3])
b=np.array([11,22,33])

np.linalg.norm(a-b)

np.float64(np.sum((a-b)**2))**0.5


def cosine(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))    


from scipy.spatial.distance import cdist
a=np.array([[1,2]])
b=np.array([[4,6]])
print(cdist(a,b, metric='euclidean'))
print(cdist(a,b, metric='cosine'))
print(cdist(a,b, metric='cityblock'))

