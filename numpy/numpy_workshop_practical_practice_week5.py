# # Activity 1: Array Creation and Inspection

# import numpy as np
# arr = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
# print(arr)
# print(np.shape(arr))
# new_arr = arr.dtype
# print(new_arr)

# # Activity 2: Indexing and Slicing

# arr1 = np.array([[1,2,3], [4,5,6]])
# print(arr1[0])

# print(arr1[0:1])
# print(arr1[1:5])
# print(arr1[2:-2])
# print(arr1[3:-1])

# print(arr1[1,1])

# arr2 = np.array([[True, False, True], [False, False, True]])
# print(arr2[0:-1])
# print(arr2[1,1])

# print(np.ndim(arr2))
# print(arr2.base)        # none because memory is allocated

# x = arr1[1:2]
# print(x.base is arr1)       # returns true this means that x is a view of arr1

# a = arr1.copy()
# b = arr1.view()
# arr1[0] = 42
# print(arr1)
# print(b)

# arr2 = np.array([[1,2,3], [4,5,6]])
# print(arr2)
# print(arr2[1])
# arr2[1] = [0]
# print(arr2)

# print(arr2.reshape(-1))


# a = np.array([1,2,3])
# print(a+10)


# arr3 = np.array([[1,2,3,4], [5,6,7,8]])
# print(arr3)

# arr4 = np.array([10, 10, 10, 10])
# print(arr3+arr4)            # use this because it uses less memory and more efficient




import numpy as np
import time 

# task 1
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
arr1[:] = 0
print(arr1)
print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype)
print(arr1.size)
# print(np.arange(1, 51))

arr2 = np.arange(0, 51, 5)
print(arr2)
print(arr2[0], arr2[1], arr2[2])        # to get first 3 elements
print(*arr2[:5])            # first 5 elements (remember this one)
print(*arr2[-2:])


# advanced numpy library 

# random integer
arr3 = np.random.randint(0, 21, 15) # start at 0, end at 20 and total of 15 elements 
print(arr3)

greater_than_10 = arr3[arr3>10]     # random numbers generated in above step with value greater 10 
print(greater_than_10)
arr3[arr3 % 2 == 0] = -1        # replacing the even numbers with -1
print(arr3)


arr4 = np.arange(25).reshape(5,5)       # 0 to 24 all elements 
print(arr4)


# understanding about view and copy
sub = arr4[0]
sub[:] = -99
print(arr)      # it will change whole array

sub = arr4[0].copy
print(arr4)


# reshaping the array and transpose the matrix

# arr5 = np.arange(1,13)
# print(arr5)

new_array = np.arange(1,13).reshape(3,4)
new_array2 = np.arange(1,13).reshape(4,3)
transpose_array = new_array2.T
print(new_array)
print(new_array2)

print(transpose_array)      # rows become columns and vice versa


ar = np.arange(9).reshape(3,3)
ar[:] = 1
print(ar)

one_d = np.array([1,2,3])
print(ar+one_d)

column_vector = np.array([[1], [2], [3]])
array_multiply = ar*column_vector
print(array_multiply)

million = np.random.rand(1_000_000)
million1 = np.random.rand(1_000_000)
print(million)
print(million1)

print(*million[:5])


# element-wise sum and product using numpy vectorization we neeed to this to compute performance and memory
start = time.time()     # saves current time before runningthe loop
sum = million+million1
product = million*million1
end = time.time()
print("vectrorized res: ", end-start)

ar1 = np.arange(5,26,5)
print(ar1)
for x in ar1:
    if x>12:
        print(x)


