# A program written in a high level programming language is called a source code
# File containing a source code is source file
# A compilation translates an entire program into machine code beforehand and a interpretation translates and executes code line-by-line at runtime
# Cpython is a combination of C and python, Jpython is a combination of Java and Python whereas Pypy is python written within a python like restricted python (a subset of python)
# A tool that lets me run a code and inspect it at each moment of execution
# Print is a function name and takes arguments that has to be string. 
    # Eg: print("Hello world") anything inside the quotes is taken as data
# Print function() begins its output from a new line each time it starts its execution and can accepts any number of arguments
# A function (it is inbulit) has particuluary two task : cause some effect and evaluate a value (return it as function's result)
# function_name(argument) checks if the name is legal, then checks if we have invoked it correctly like kept correct arguments, next jumps to the desired function and executes the code.
# \n is a newline character where 'n' is a keyword and its task is that it escapes the exisiting line and print it in next output line.
# End keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments or in another way the end keyword is same like /n (it's task) and it's syntax is end=" "
# The sep (like seperator) seperates its outputted arguments with spaces
    # print("My", "name", "is", "Monty", "Python.", sep="-")
    # outputs: My-name-is-Monty-Python. (you can change the "-" to anything)
# A literal is data whose values are determined by the literal itself and we use them to encode data and to put them into your code. For example 1234 is a literal whereas c is not a literal.
    # Example : print("2") will store it in as a string
    # Example : print(2) and  this one will be converted to machine representation (a set of bits) that is readable to humans.
# An octal number is representated by 00 or 0o this means that the digits may be contained from 0 to 7 only. Example: 0o123 is converted as 83 and this can be done by python's print function
# A hexadecimal number is that which has a (decimal) value equal to 291.
# 4 is an integer whereas 4.0 is a floating point number and sometimes the python compiler uses this literal as we try to print(0.0000000000000000000001) it gives 1e-22 where e is the exponet and -22 is the power of 10.
# Boolean values in python are True and False 
# None is called as "NoneType" object and it represents the absence of value
# Data and operators when connected together form expressions. The simplest expression is a literal itself. 
# Here the operators are mathematical ones (+, -, *, /, //, %, **) and the exponentiation operator( ** ) accepts left argument as base and right as exponent.
# Example : (remember it as square root)
    # print(2 ** 3) // prints 8
    # print(2 ** 3.) // prints 8.0
    # print(2. ** 3) // prints 8.0
    # print(2. ** 3.) // prints 8.0
# for multiplication operator (*)
    # Example:
        # print(2 * 3) // prints 6
        # print(2 * 3.) // prints 6.0
        # print(2. * 3) // prints 6.0
        # print(2. * 3.) // prints 6.0
# For division operator (/) the A / (slash) sign is a divisional operator the value in front of the slash is a dividend, the value behind the slash, a divisor also the value given by the division operator is always a float.
    # Example:
        # print(2 / 3) // prints 0.66
        # print(2 / 3.) // prints 0.66
        # print(2. / 3) // prints 0.66
        # print(2. / 3.) // prints 0.66
# An interesting operator known as integer divisional operator (//) or floor division and the results are always rounded. An integer by integer will give you only integer value and rest others will give us floating value only.
# Example:
        # print(6 // 3) // prints 2
        # print(6 // 3.) // prints 2.0
        # print(6. // 3) // prints 2.0
        # print(6. // 3.) // prints 2.0

        # print(6 // 4) // prints 1 rounding goes toward the lesser integer val.
        # print(6. // 4) // prints 1.0
        # print(-6 // 4) // prints -2
        # print(6. // -4) // prints -2.0 
# Reminder (%) always prints remainder left after the integer division
# Addition operator (+)
# Example:
        # print(-4 + 4) // prints 0
        # print(-4. + 8) // prints 4.0
        # print(-4 -4) // print -8
        # print(-4. -4) // print -8.0
# Binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.
# Example: print(9 % 6 % 2) will print 9%6 as 3 and then 3%2 as 1 and it's always left side binding only. print(2 ** 2 ** 3) prints 64 (2**2 and then 4**3)
# Priority of the operators (from left being as the highest one and right most as the lowest one)
    # {**, (+, -) [UNIARY], (*, /, //, %), (+, -) [BINARY]}
# Paranthesis are always calculated first 
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] they are "reserved keywords" or they are predefined
# Shortcut operators or compound assignment operators are like x=x+1 as x++, x*=2 as x=x*2 and so on and remember that each variable must have a unique name as identifier.

# Input function()
# It prompts the user to input some data while the code is still running and the result of a input function is always string
# Typecasting from integer to float or vice-versa can be done as 
    # x = float(input("Enter a number: "))
    # y = x ** 2.0
    # print(x, "to the power of 2 is", y)
# it takes input as (example) -- 5
# output is 5.0 to the power of 2 is 25.0 and if i enter -5 then also ans is 25

# String 
# concatentation :
    # we can add two strings as string1+string2
# type conversion(str):
    # converts a number to string and is possible through str like str(number)

# Replication operator happens when we apply it to a string and number or a number and a string. Ex-- "James" * 3 gives "JamesJamesJames" and 3 * "an" gives output as "ananan". A number less than or equal to 0 prints empty string.
# The assignment operator (=) assigns value to a variable. Ex - a=b and the equals to operator (==) compares and returns boolean values like is the value on the left hand side is equal to the right hand side or not?
    #Example 
            # var = 0  # Assigning 0 to var
            # print(var == 0) // prints True
            # var = 1  # Assigning 1 to var
            # print(var == 0)   // prints False
# Comparison operator (>= or <=) checks if the value is greater than or less than the value on the right side and stores in memory 
# The priority table is as:
        #Priority	Operator	
        #1	        +, -	        unary
        #2	        **	
        #3	        *, /, //, %	
        #4	        +, -	        binary
        #5	        <, <=, >, >=	
        #6	        ==, !=
# If-else (condtional statements) checks if the value satisfy the condition or not. The syntax is if(statement>statement2): print("True") else: print("False") and the use of this is known as nesting.
# Nested if-else statement is where we put an if block inside a if block and also we can put else inside an else block!
# The elif statement is used to check for the necessary condition that is more than once and stop it when the condition is meet.
# The example of what is the largest of two numbers can be make using if-else condition (if number1>number2: print("bigger") else: print("smaller")
# Performing a certain part of the code more than once is called a loop.
# The built-in function [max() and min()] is used to find the largest and smallest of all numbers. Example: max(11,12,23) will print 23 and 11 as resp.
# The built-in function round() rounds a floating-point number to a specified number of decimal places.
# Example of wheather a year is a leap year or not is 

# year = int(input("Enter a year: "))
#if year < 1582:
#   print("Not within the Gregorian calendar period")  
#else: 
#    if year %4 !=0:
#        print("Common year")
#    elif year %100 !=0:
#        print("Leap year")
#    elif year %400 !=0:
#        print("Common year")
#    else:
#        print("Leap Year")
# prints [year = 2000 then it will show Leap Year]
# While loop repeats the execution as long as the condition evaluates to true and performs the statement only once
# Syntax of while loop:
    # while conditional_expression:
        # instruction_one
        # instruction_two
        # instruction_three

# Example: count how many numbers are odd and even
# odd_numbers , even_numbers = 0,0
# number = int(input("Enter a number: "))
# 0 terminates execution.
# while number != 0:
    # if number % 2 != 0:
        # odd_numbers += 1
    # else:
        # even_numbers += 1
    # read the next number
    # number = int(input("Enter a number: "))
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)
# prints like (inter input okkk so---- 5,4,3,2,1,0 (to stop)) then we get output as odd number count as 3 and even number count as 2 

# For loop ( here the "for" is a keyword and any variable after the for keyword is control variable and "in" keyword describes the range of possible values that are assigned to the control variable and it is designed to browse large collection of data item by item. The range() function is responsible for generating all the desired values of the control variable. The pass keyword inside the loop is an empty instruction (does nothing at all).
# Example: 
    # for i in range(2, 8):
        # print("The value of i is currently", i)
# prints 2,3,4,5,6,7
# The range function also accepts three arguments (the third argument is the increment one default value of the increment is 1) and the range's second argument must always be greater than the first one and in ascending order!
# "break" keyword exits the loop immediately and unconditionally ends the loop's operation and executes after the loop's body whereas "continue" keyword behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.
