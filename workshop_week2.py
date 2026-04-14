# Activity 1: Lambda Functions and Functional Patterns

# # lambda function in python
# it can have any number of arguments but only have one expression
# anonymous function
# particuluary used inside a mao or list
# def square(x):
#     return x*x
# print(square(5))

# list_lambda=lambda s:[x**2 for x in range(20)]
# print(list_lambda(5))

# nums=[1,2,3,4,5]
# squared=list(map(lambda x:x**2, nums))
# evens=list(filter(lambda x:x%2==0, nums))
# print(evens)
# print(squared)

# [2,4,6]
# [1,4,9,16,25]

# nums=[1,2,3,4,5,6]
# tripled=list(map(lambda x: x*3, nums))
# evens=list(filter(lambda x: x%2==0, nums)) # returns boolean
# print(tripled)
# print(evens)



# # Comprehensions (List, Set, Dict)

# offers a shorter syntax when you want to create a new list based on the values of an existing list

# # list comprehension

# squares_of_even = [x**2 for x in range(10) if x%2==0]
# print(squares_of_even)

# compare= ["Small" if x**2<15 else "Large" for x in range(10) if x%2==0]
# print("Compare")

# syntax: [expression for item in some_iterable if some_condition]

# # Dictionary comprehension

# words = ['Apple', 'Banana', 'Cherry']
# word_lengths={word: len(word) for word in words if word != 'Carrot'}
# print(word_lengths)

# # Set comprehension

# words = ['Apple', 'Banana', 'Cherry']
# word_lengths={word: len(set(word)) for word in words if word != 'Carrot'}
# print(word_lengths)

# return how many vowels are present in a string

# string='I am Optimus Prime'
# vowels = {x for x in string.lower() if x in 'aeiouAEIOU'}
# print(vowels)


# # Object-Oriented Programming – Classes and Constructors

# class Dog:
#     def __init__(self, name, breed):
#         self.name=name # a refreence to the object itself and store them as attributes
#         self.breed=breed

# my_dog=Dog('Voyage', 'Beagle')
# friend_dog= Dog('Butcher', 'Lambarodor')
# print(my_dog)
# print(friend_dog)
# print(my_dog.name, 'is a', my_dog.breed)
# print(friend_dog.name, 'is a', friend_dog)


# # Default parameters in constructor

# class Circle:
#     def __init__(self, radius=1):
#         self.radius=radius
    
# npc_circle=Circle()
# print(npc_circle.radius)
# sentient_circle=Circle(radius=9)
# sentient_circle.radius=20
# print(sentient_circle.radius)


# class Student:
#     def __init__(self, name, grade='A'):
#         self.name=name
#         self.grade=grade

# s=Student('Alex')
# s2=Student('Frodo', 'A+')
# print('Name:', s.name, '\nGrade:', s.grade)
# print('Name:', s2.name, '\nGrade:', s2.grade)


# # Designing Methods with self

# class Dog:
#     def __init__(self, name, breed):
#         self.name=name
#         self.breed=breed
#     def describe(self):
#         # return a string to define dog
#         return f'{self.name} is a {self.breed}' # formatiing

# my_dog=Dog('Voyager', 'Beagle')
# print(my_dog.describe())

# class Counter:
#     def __init__(self):
#         self.count=3

#     def increment(self):
#         self.count+=1

#     def decrement(self):
#         self.count-=1

# count=Counter()

# count.decrement()
# print(count.count)
# # count.increment()

# count.decrement()
# print(count.count)
# # count.increment()

# count.decrement()
# print(count.count)



# # Operator Overloading (Introductory)

# class Book:
#     def __init__(self, title):
#         self.title=title
#     def __str__(self):
#         return f'Book: {self.title}' # "Book "+self.title
#     def __repr__(self):             # use for developers
#         return f'Book (dev)({self.title})' 
    
# b=Book('1989')
# print(b)


# __add__ override

# class Vector:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
    
#     def __str__(self):
#         return f'{self.x}, {self.y}'
    
# v1 = Vector(2,3)
# v2 = Vector(4,5)

# v4 = Vector(5,6)
# v5 = Vector(1,12)
# v3 = v1 + v2
# v6 = v4-v5

# print(v3)
# print(v6)
# # not implement method can be used 



# # Code Style & Readability

# def bad_square(x): 
#     return x**2
# print(bad_square(9))

# # Testing Functions and Modules
# def multiply(x,y):
#     return x*y

# assert multiply(2,3) ==6, "oh no error" # if there is an error it will jump out of the loop and it can be used in testing frameworks
# print("all good")