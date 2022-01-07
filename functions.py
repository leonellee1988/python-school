input = raw_input

"""
Functions in Python:

A Python function has the following features:

a) The keyword "def"
b) A function name
c) Paranthesis
d) A colon
e) Code to execute
f) A return statment

In this little class we are going to check some specific Python's functions,
and we also will learn how to create our own functions

"""

# max()function: take numbers or any kind of iterable as arguments, and return the greater item

print(max(18,15,-9,100))#Return: 100

my_list = [21,1500,-2000,0,4]
print(max(my_list))#Return: 1500

#What if we pass letters in a max()function... well, Python will compare their ASCII values

print(max('a','b','c','d','e'))#Return: e

# min() function: as you can imagine, this function is the opposite of max() function

print(min(18,15,-9,100))#Return: -9
print(min(my_list))#Return: -2000
print(min('a','b','c','d','e'))#Return: a

# divmod() function: return the quotient and remaninder when dividing two numbers

print(divmod(7,2))#Return(3,1)

# len() function: return the length (number of items) of an object (string, array or dictionary)

print(len(my_list))#Return: 5

my_str = "Hello world, we are practicing Python functions"
print(len(my_str))#Return: 47

my_tuple = (10,20,30,40,50,60,70,80,90,100)
print(len(my_tuple))#Return: 10

my_dictionary = {
    'name': 'Edwin',
    'last-name': 'Lee',
    'age': 33,
    'subject':'Python',
    'grade':95
}

print(len(my_dictionary))#Return: 5

# input() function: this function lets the user to enter information

my_age = input("Enter your age: ")

#It's important to know the type of data that the user enters. Do it with the function type()

print(type(my_age))

#We could think the data entered is an integer, but it is not, it is a string <type 'str'>

#How can we change the type of the data? With other functions of course:

my_age_02 = int(input("Enter your age (again): "))
bank_account = float(input("How much money do you have in the bank: "))

print(type(my_age_02))#Return: <type 'int'>
print(type(bank_account))#Return: <type 'float'>

#Now it is the time to create our own functions...

#Without arguments:

def my_message():
    message = "Hello world, keep coding with Python"
    return message

print(my_message())#Return: Hello world, keep coding with Python

def sumNumbers():
    num_01 = 50
    num_02 = 80
    sum = num_01 + num_02
    return sum

print(sumNumbers())#130

#With arguments:

def my_message_02(message):
    return message

print(my_message_02("Hello world, keep coding with Python"))
#Return: Hello world, keep coding with Python

def sumNumbers_02(num_01,num_02):
    sum = num_01 + num_02
    return sum

print(sumNumbers_02(50,80))#130