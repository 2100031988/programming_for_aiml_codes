# <---------- What is numpy and why do we need it ---------->
# they are used to create array and working with it 

# they are faster than arrays (50x) that's why preferred than list
# object creation is done using ndarray

# <---------- why are they fast??? ---------->
# numpy arrays are stored in continuous place in memory so processes can access and manipulate them very efficiently.


from typing import Any
import numpy as np
from numpy import random

# <----- 1. creating an array ----->
arr = np.array([1,2,3,4,5])
print(arr)

print(np.arange(1, 51))       # will create an array of elements from 1 to 50


# <----- 2. type of array ----->
print(type(arr))    # <class 'numpy.ndarray'>


# <----- 3. 2d array and 3d array ----->
arr = np.array([[1,2,3], [4,5,6]])
arr = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])


# <----- 4. Number of dimenions ----->
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# <----- 4. Number of dimenions using arguments for a higher dimension array ----->
arr1 = np.array([1,2,3,4], ndmin=5)
print(arr1)
print("dimensions :" , arr1.ndim)


# <----- 5. Accessing element for an array ----->
arr2 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(arr2[1,0,1])


# <----- 6. Slicing an array ----->
# slicing can be done like [start:end]
# we can also do using step function [start:end:step]

# -- if we don't indicate "start" it is considered as 0, "end" will take default as 1
# -- if we don't assign value of "step" it takes default as length of the array 

arr3 = np.array([1,2,3,4,5,6,7])
print(arr3[1:5])     # remember that 1 is included but 5 is not included....... output as : [2,3,4,5] so no 6
print(arr3[4:6])     # [5,6]
print(arr3[3:])
print(arr3[:2])

# negative slicing
print(arr3[1:-1])
print(arr3[4:-2])
print(arr3[:-3])
print(arr3[-1:])

# slicing using step function
print(arr3[1:5:2])
print(arr3[3:6:1])
print(arr3[4::7])
print(arr3[:4:3])
# print(arr3[5:7:0])  # slice step cannot be zero
print(arr3[0:0:2]) # empty array


# slicing an 2 d array
arr3_1 = np.array([[1,2,3], [4,5,6]])
print(arr3_1[0, 1:2])
print(arr3_1[1, 0:2])
print(arr3_1[0:2, 2])     # return two elements from both of the array
print(arr3_1[1:2, 1:4])


# <----- 7. Datatype ----->
arr4 = np.array([1,2,3,4,5])
print(arr4.dtype)


arr5 = np.array(['apple', 'banana', 'cherry'])
print(arr5.dtype)


# creating a array with a defined datatype
arr1_1 = np.array([1, 2, 3, 4], dtype='S')

print(arr1_1)
print(arr1_1.dtype)
 

# <----- 7. Converting data type of existing arrays ----->
arr6 = np.array([1.1, 2.1, 3.1])

newarr = arr6.astype('i')
print(newarr)


# <----- 8. Difference between copy and view ----->
# copy is a new array (if you make any changes to the original array or to copy will not affect the new array
# view is just a view of original array and if you make any changes those chnages will affect the view

# copy 
ar = np.array([1,2,3,4,5])
x: np.ndarray[tuple[Any, ...], np.dtype[Any]] = ar.copy()
ar[0]=42
print(ar)
print(x)    # even though you made changes and this will not show that change

# view
a1 = np.array([1,2,3,4,5])
y = a1.view()
a1[0] = 42
print(a1)
print(y)        # you made changes and this will show that change

# copy owns the data but view does not own the data


# <----- 9. Shape of an array ----->
ar1 = np.array([[1,2,3], [4,5,6]])  # remember that it returns tuple data type
print(arr.shape)        # prints the dimension of an array here output is (2,4) meaning 2 rows and 4 colunns


ar2 = np.array([1,2,3,4], ndmin=5)
print(arr2.shape)




# <----- 9. Reshaping an array ----->
# reshapping an array means changing the dimension of an array
# we can add or remove dimensions or change number of elements in each dimension

# from 1 d to 2d
ar3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(ar3.reshape(4,3))     # note that total elements should remain the same (4*3 = 12) always

# from 1 d to 3d
ar4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(ar4.reshape(2,3,2))

print(ar4.reshape(2,6).base)    # this base will give you if it view or copy (here it is view as it returns original array)

print(ar4.reshape(2,3,-1))  # this -1 indicates that numpy will allocate it automatically so here it will be 2 
                            # we can not pass -1 in more than one argument 



# <----- 10. Flattening an array ----->
# converting a 2d array into 1d array

ar5 = np.array([[1,2,3,4], [5,6,7,8]])
newarr1 = ar5.reshape(-1)
print(newarr1)


a4 = np.array([[1,2,3,4], [5,6,7,8]])

method_1 = a4.flatten()         # flatten in just one step
print(method_1)      # converting a 2d array into 1d array

method_2 = a4.ravel()         # using ravel also converts in just one step bro
print(method_2)      # converting a 2d array into 1d array



# <----- 11. Iterating arrays ----->
# using for loop

ar6 = np.array([1,2,3])     # for 1d array
for x in ar6:
    print(x)

ar7 = np.array([[1,2,3],  [4,5,6]])     # for 2d array
for x in ar7:
    print(x)

ar8 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in ar8:
  for y in x:
    for z in y:
      print(z)          # in 3d we have to iterate in each dimension


# we can use nditer() for this as it can convert from basic to very advanced iterations

for y in np.nditer(ar8):        # using on a 3d array
   print(y)


# we can use p_dtypes to iterate through different datatypes
ar9 = np.array([1, 2, 3])

for z in np.nditer(ar9, flags = ['buffered'], op_dtypes=['S']):
   print(x)


# iterating With different step size
a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(a1):
   print(x)


# ndenumerate() : Give me index + value for each element
a2 = np.array([1,2,3])
for idx, x in np.ndenumerate(a2):
   print(idx, x)


# same with 2d and 3d also 
a3 = np.array([[1,2,3],  [4,5,6]])  
for idx,x in np.ndenumerate(a3):
   print(idx, x)




# <----- 12. Joining arrays ----->

# using concatenating
arr7 = np.array([1,2,3])
arr8 = np.array([4,5,6])

arr_new_new = np.concatenate((arr7, arr8))

# axis = 1 → columns (horizontal join)
# axis = 0 → rows (vertical join)

arr_1 = np.concatenate((arr7, arr8), axis=0)
print(arr_1)

# the stack function helps us to understand that it concatenates the string and also add the 
arr10 = np.array([4,5,6])
arr9 = np.array([1,2,3])

newarr2 = np.stack((arr9, arr10), axis = 1)     # axis adds the dimension too
print(newarr2)
# we can use hstack for along the rows and vstack along the columns
# the dstack function converts it into 3d dimension and is in more depth
arr = np.dstack((arr9, arr10))




# <----- 12.   Spliting arrays ----->
# just an reverse of joining

# array_split
arr9 = np.array([1,2,3])
arr10 = np.array([4,5,6,7,8,9])

newarr3 = np.array_split((arr9), 3)
print(newarr3)

newarr4 = np.array_split((arr10), 6)
print(newarr4)
print(newarr4[0])

# splitting an 2d array
arr11 = np.array([[1,2,3,4], [5,6,7,8]])
newarr5 = np.array_split(arr11, 3)
print(newarr5)

# we can use axis for along side the columns and rows as well
newarr6 = np.array_split(arr11, 3, axis=1)   # use hsplit and vstack as well
newarr7 = np.hsplit(arr11, 3)



# <----- 13. Searching in an array ----->

arr12 = np.array([1,2,3,4,5,4,4])
x1 = np.where(arr12 == 4)     # if element is present or not
print(x1)

x2 = np.where(arr%2 == 0)     # for odd positions
print(x2)

x3 = np.where(arr%2 == 1)    # for even positions (remember that position and the element in the array)
print(x3)

# searching in a sorted array
ar10 = np.array([1,2,3,4,5,6,7,8,9])
x4 = np.searchsorted(arr10, 7)
print(x4)

# search from the right side and left side
x5 = np.searchsorted(arr10, 3, side='right')
x6 = np.searchsorted(arr10, 5, side='left')

# searching for multiple values
x7 = np.searchsorted(arr10, [2,4,6])



# <----- 14. Sorting an array ----->
ar11 = np.array([3,2,0,1,4])
print(np.sort(arr11))

arr12 = np.array(['banana', 'cherry', 'apple'])    # sorting alphabetical vise
print(np.sort(arr12))

arr13 = np.array([True, False, True])        # sorting boolean array
print(np.sort(arr13))

arr14 = np.array([[3, 2, 4], [5, 0, 1]])     # sorting a 2d array (both arrays will be sorted)
print(np.sort(arr14))



# <----- 15. Filtering an array ----->
# getting some elements out of an existing array and creating out a new array out of them is called filtering
# in numpy we filter an array using a boolean index list and If the value at an index is True that element is contained
# in the filtered array, if the value at that index is False that element is excluded from the filtered array.

arr15 = np.array([41, 42, 43, 44])
x8 = [True, False, True, False]
newar8 = arr[8]
print(newar8)     # returns [41, 43] becuase those are true


# creating filter directly from array 
filter_array = arr15 > 42

filter_arr = arr % 2 == 0     # for only even elements
filter_arr = arr % 2 == 1     # for only odd elements
newar9 = arr[filter_array]
print(filter_array)
print(newar9)



# <----- 16. Broadcasting an array ----->
# NumPy automatically makes arrays compatible for operations (like addition, subtraction, etc)

a = np.array([1,2,3])      # simple example
print(a+10)

b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([10, 20, 30])
print(b+c)     # so first of all c we will changed as ([10,20,30], 
                                                      # [10,20,30]) to allocate space and then it will add it

                                                      

# <----- 17.  Vectorised Operations and ufuncs ----->

# element-wise arithmetic 
x = x+2 

# universal functions (e.g., np.sqrt, np.exp, np.maximum)
a1 = np.array([1,2,3,4,5])
sin_a1 = np.sin(a1)
print("sin: ", sin_a1)     # don't use sin(90)[no radians in numpy] --> np.sin(np.radians(90)) use this one

cos_a1 = np.cos(a1)
print("cos: ", cos_a1)

tan_a1 = np.tan(a1)
print("tan: ", tan_a1)

sqrt_a1 = np.sqrt(a1)
print("sqrt: ", sqrt_a1)

exp_a1 = np.exp(a1)
print("exp: ", exp_a1)

log_a1 = np.log(a1)
print("log: ", log_a1)     # don't use log(0) or log(-1)



# shortcuts to remember
arr2 = np.arange(1, 51)
print(*arr2[:5])     # prints first 5 elements
print(*arr2[:3])     # prints first 3 elements
print(np.arange(0, 51))    # prints 0 to 50 elements
print(np.arange(0, 51, 5))  # prints 0 to 50 and with a step of 5 
print(*arr[-2:])     # last two elements


x9 = random.randint(100, size=(3,5))      # create an array (random) of size 3,5

# sorting
print("quicksort", np.sort(arr, kind = 'quicksort'))
print('mergesort', np.sort(arr, kind = 'mergesort'))