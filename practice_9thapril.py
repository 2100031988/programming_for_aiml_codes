import numpy as np
# creating an array
arr = np.array([1,2,3,4,5])
arr1 = np.arange(1,51)
print(arr)
print(arr1)

# type of an array
print(type(arr1))

# number of dimensions
print(np.ndim(arr))

arr2 = np.array([[1,2,3], [4,5,6]])     
print(arr2)
print(np.ndim(arr2))

# slicing an array
print(arr2[-1:3])       # this is same as 1:3 because -1 becomes end second is (4,5,6)
print(arr2[0:0])        # empty list and if start == end then you will always get empty list
print(arr2[1:0:2])



