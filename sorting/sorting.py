# sorting algorithms 

# -- arranging values


# <----- Activity 1 : SORTING ALGORITHMS----->
# <----- Built in sorting functions ---->

# sorted()
# creates new sorted list

arr = [88, 92, 75, 91, 85]
score = sorted(arr)

print(score)        # new sorted list
print(arr)          # but original list still unchanged


# list.sort()
# changes original list

arr.sort()          # it sorts the original array
print(arr)

# descending order
new_array = sorted(arr, reverse=True)
print(new_array)       # this sorts the array in descending order 


# <----------------------------------------------------->

# Bubble sort
# it compares the neighboring elements and then swap them if it is less 
# than the element or not

arr2 = [10, 2, 0, 5, 15]
def bubble_sort(arr2):
    n=len(arr2)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr2[j]>arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
    return arr2

print(bubble_sort(arr2))


#  <----------------------------------------------------->


# list vs numpy array
# -- numpy is better and we can store same ones at the same place and other
# at different arrays.

#  <----------------------------------------------------->


# sorting key functions

# 1. string by length

words = {"apple", "orange", "banana", "kiwi"}
sorted_words = sorted(words, key = len)

print(sorted_words)     # sorting based on length of the string here fruits


# 2. sort tuples
students = [("John", 90), ("Alice", 85), ("Bob", 95)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# | Algorithm      | Best       | Worst      | Stable | Fast?     |
# | -------------- | ---------- | ---------- | ------ | --------- |
# | Bubble Sort    | O(n)       | O(n²)      | Yes    | No        |
# | Selection Sort | O(n²)      | O(n²)      | No     | Slow      |
# | Merge Sort     | O(n log n) | O(n log n) | Yes    | Fast      |
# | Quick Sort     | O(n log n) | O(n²)      | No     | Very Fast |
# | Timsort        | O(n log n) | O(n log n) | Yes    | Excellent |


#  <----------------------------------------------------->

# numpy operations 

# import numpy as np
# arr = np.array([1,2,3])
# print(arr)

# we can see that matrics are far better in numpy due to high memory efficient
# also suitable for operations in array


# <----- Activity 2 : SEARCHING & SELECTION ----->

# Linear Search
# check elements one by one

arr = [88, 92, 75, 91, 85]
print(sorted(arr))

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(linear_search(arr, 75)) # it checks every element and 
# the time complexity is o(n)


#  <----------------------------------------------------->

# Binary Search
# it works only on SORTED ARRAY
# it divides the array into half and not check every element

def binary_search(arr, target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1


#  <----------------------------------------------------->

# Bisect module
# to insert an element in a sorted list

import bisect

arr = [1,2,4,5]
bisect.insort(arr, 3)
print(arr)      # will insert 3


#  <----------------------------------------------------->


# kth smallest element
# finds the kth smallest value like find the second smallest,
# thrid smallest element, etc

arr1_1=[7,2,9,1]
k=2 # which position of the element to find

arr.sort()
print(arr[k-1])


#  <----------------------------------------------------->

# Numpy search functions

# 1. find indices greater than 10

import numpy as np
arr = np.array([5, 15, 7, 25, 10])

find_element = np.where(arr>10)     # logic to see if there is an element > 10
print(find_element)

# numpy search has better advantages as it is
# vectorized, faster, supports multidimensional arrays
# and optimised for memory handling

#  <----------------------------------------------------->


# <----- Activity 3 :  TOP-k & RANKING ----->

# Full sort vs partial sort
# full sort sorts the entire array and partial sort 
# only finds top kth value, faster for larger datasdets



# Top-k using numpy

import numpy as np
                # [0, 1, 2, 3, 4]
scores = np.array([88, 92, 75, 91, 85])
                #  [2, 4, 0, 3, 1]

top_indices = np.argsort(scores)[-2:]   # returns indices that would sort array in ascending order
            # take the last two largest number and it gives [3, 1] -- [91, 92]

print(top_indices)
print(scores[top_indices])


#  <----------------------------------------------------->

# Ranking using argsort()

                # [0, 1, 2, 3, 4]
scores = np.array([88, 92, 75, 91, 85])

ranks = scores.argsort().argsort()
        # first argsort will sort it in ascending order
        # [2, 4, 0, 3, 1] -- [75, 85, 88, 91, 92]
        # second argsort asks where does each position land in the sorted order.

        # Score 88  → rank 2  (3rd lowest)
        # Score 92  → rank 4  (highest)  ✓
        # Score 75  → rank 0  (lowest)   ✓
        # Score 91  → rank 3  (2nd highest)
        # Score 85  → rank 1  (2nd lowest)

        # gives rank on the result

print(ranks)


#  <----------------------------------------------------->


# <----- Activity 4 :  NUMERICAL GRADIENT ----->
# gradient means change and how fast is it changing??

# analytical vs numerical gradient
# analytical -- exact mathematical derivative
# numerical gradient -- approximation using nearby values

# Finite Difference Method
# manual gradient code

x = np.linspace(0, 10, 100)
y = np.sin(x)

grad = np.gradient(y, x)
print(grad)


#  <----------------------------------------------------->

# find median and searching median

# median
arr3 = np.array([5, 7, 1, 2, 0, 10])
median = np.median(arr3)
print(median)

found = median in scores
print(found)

# mode
mode = np.mode(arr3)
print(mode)


