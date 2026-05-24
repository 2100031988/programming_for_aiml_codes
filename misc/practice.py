# understand the use of fstrings
# an easy way to put variables inside a sentence

# name=input()
# age=int(input())
# print(f"My name is {name} and I am {age} years old")
# print(f"3+2={3+2}")

# string="Sabya, kumar"
# print(string.lower())
# print(string.upper())
# print(string.replace("kumar", "singh"))
# print(string.count("a"))
# print(string.isalnum()) # checks if all the characters are alphabetic
# print(string.capitalize()) # converts first character to capital letter
# print(string.find("kumar")) # comma and space are counted so outputs 7 and returns -1 if not found (remember this bro)
# print(string.find("a", 5, 10)) # output 9 and yes both 5 and 10 are counted
# # isdigit(), isalnum() tocheck if there is alphanumeric both letters, numbers
# print(string.startswith("sabya")) # output true
# print(string.endswith("singh")) #output false
# # strip () removes leading and trailing whitespace, lstrip() and rstrip()


# # casting
# x=10
# y=20.5
# z="30"
# float_from_int=float(x)
# integer_from_float=int(x)
# string_from_float=str(z)


# # if-elif-else block
# weather="sunny"
# activity = "picnic" if weather =="sunny" else "indoor games" # continued if-else block in a single sentence


# def greet(name):
#     message=f"Hello, world!"
#     print(message)

# greet("Sabya")

# # list [] and ordered.... are mutuable (changable and allow duplicates)
# fruits=["apple", "orange", "banana"]
# print(fruits)
# print(fruits[0]) # apple

# for fruit in fruits:
#     print(fruit)    

# print(len(fruits)) # 4
# print("apple" in fruits) # true

# fruits[0]="pineapple"
# for fruit in fruits:
#     print(fruit)

# # append to add another element
# fruits.append("pineapple")

# # remove
# fruits.append("apple")
# # insert
# fruits.insert(0, "apple")
# # sort
# fruits.sort() # in alpahbetical order
# # reverse
# fruits.reverse()
# # index
# fruits.index("apple")
# # count
# fruits.append("pineapple")


# # set unordered, immutable (cannot change like add or remove elements)
# fruits={"apple", "orange", "coconut"}

# # add
# fruits.add("grapes")
# # remove
# fruits.remove("apple")
# # pop
# fruits.pop() #removes element but it can random also
# fruits.clear()


# tuple ordered, unchangable, duplicates okkk and  fastern than list

# fruits=("apple", "orange", "coconut")

# #index
# print(fruits.index("apple"))
# # count
# fruits.count("orange")

# for fruit in fruits:
#     print(fruit)



# # dictionary a collection of key:value pair, ordered and changeable, no duplicates

# capitals={"USA":"washington dc ", 
#           "India":"new delhi",
#           "china":"bejing", "russia":"moscow"}

# # gets the value
# capitals.get("USA")
# # if not there then none
# capitals.get("Japan") # none

# # update
# capitals.update({"Germany":"Berlin"})
# # delete
# capitals.pop("china")
# capitals.popitem() # removes latest item or thw last item
# capitals.clear()
# keys=capitals.keys()
# print(keys) # returns all keys 

# for key in capitals.keys():
#     print(key)


# values=capitals.values()
# for value in capitals.values():
#     print(value)

# items=capitals.items() # 2d ojbect so this is like it returns tuple [(), (), ()]

# for key, value in capitals.items():
#     print(f"{key} : {value}")
# # output as 
# # USA: Washington
# # India: New delhi



# working on files
# read and open a file

# reading -- opening files with open()
# with open('/Users/sabyasachi/Documents/programming_for_ai/test.txt') as file:
#     print(file.read())

# print(file.closed) # so normally when you read a file it closses iteself so this is just for checking

# so if we write with open('test.tx') this will raise an filennotfound error
# to acoid this we will use try and except

# try: 
#     with open('/Users/sabyasachi/Documents/' \
#     'programming_for_ai/test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("file was not found")


# write files 
# txt_file="i like pizza"
# file_path="output.txt"

#  # with is a statement and w is for writing but if there is suppose 'x' so this will write that file if it is already not exist then it will create but if it is already there then there will be a error fileexisterror
# try:
#     with open(file_path, "w") as file: 
#         file.write(txt_file)
#         print(f"txt file {txt_file} was created")
# except FileExistsError:
#     print("that file already exist")



# employees=["Sabya", "Sam", "Alex", "Pat"]
# file_path='/Users/sabyasachi/Documents/output.txt'

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee+" ")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("alreaduy exist")


# --------- .json ---------

# import json

# employee = {
#    "name": "Spongebob",
#    "age": 30,
#    "job": "Cook"
# }

# file_path = "output.json"

# try:
#     with open(file_path, 'w') as file:
#         json.dump(employee, file, indent=4)

#     print(f"JSON file '{file_path}' has been created successfully")
# except FileExistsError:
#     print("That file already exists!")


# # --------- .csv---------
# import csv

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployed"],
#              ["Sandy", 27, "Scientist"]]

# file_path = "output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

 




# understanding about class 
# class Compare:
#     def add(self, other):
#         "returns the addition of two complex numbers: real and imaginary"
#         return self.r + other.r + self.i + other.i
# x1,x2=Compare(3.0, -4.5), Compare(-2.0, 5.5)
# x1.add(x2)



