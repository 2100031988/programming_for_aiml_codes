# practicing numpy 
import numpy as np
# array
arr = np.array([1,2,3,4])
print(arr)

arr1 = np.arange(1, 51)
print(arr1)

arr2 = np.random.randint(50)
print(arr2)

# number of dimensions
print(np.ndim(arr))

# type of array
print(np.dtype)

# indexing and slicing in array 2d , 3d
arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d)

arr_1d = np.array([1,2,3,4,5])
print(arr_1d[1:-1])
print(arr_1d[0:-2:2])
print(arr_1d.max())
print(arr_1d.min())

print(arr_1d.size)

arr_astype = np.array([1, 2.0, 3.5, 4., 0.33333])
print(arr_astype.astype(np.int_))

arr_3d = np.array([1,2,3,4], ndmin=2)   # dimension for higher array it is efficient
print(arr_3d)


# copy and view
a1 = np.array([1,2,3,4,5])
y = a1.view()
a1[0] = 42
print(a1)
print(y)

a2 = np.array([1,2,3,4,5])
x = a1.copy()
a1[0] = 42
print(a1)
print(x)


a3 = np.array([[[1,2,3], 
                [4,5,6]], 
               [[7,8,9], 
                [10,11,12]]])
print(np.shape(a3)) or a3.shape


a4 = np.array([[1,2,3], [5,6,7]])
method_1 = a4.reshape(-1)       # reshapeing the array but passing -1 as the argument
print(method_1)      # converting a 2d array into 1d array

method_2 = a4.flatten()         # flatten in just one step
print(method_2)      # converting a 2d array into 1d array

method_3 = a4.ravel()
print(method_3)      # converting a 2d array into 1d array



a5 = np.array([[1,2,3], [4,5,6]])
for idx, x in np.ndenumerate(a5):       # print the array in 2d format with the idex and elements inside it
    print(idx, x)


# new_arr = np.concatenate(a4, a5)
# new_arr_rows = np.concatenate((a4, a5), axis = 0)



a4 = np.array([[1,2,3], [5,6,7]])              
a5 = np.array([[1,2,3], [4,5,6]])
print(a5.flatten())
print(a4.flatten())

stack_function = np.stack((a4, a5))
print(stack_function)

hstack_function = np.hstack((a4, a5))
print(hstack_function)

vstack_function = np.vstack((a4, a5))
print(vstack_function)


a5 = np.array([[1,2,3], [4,5,6]])
x1 = np.where(a5==4)
print(x1)

x2 = np.searchsorted(a5.flatten(), 3)       # flattening becuase it is a 2d array
print(x2)
print(np.sort(a5))  
print(a5>2) # filtering an array