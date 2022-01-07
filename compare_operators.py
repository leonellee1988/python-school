"""
Comparison operators in Python:

1) If the values of two operands are equal, use ==
2) If the values of two operands are not equal, use !=
3) 1) If the value of left operand is greater than the
value of right operand, use >
4) If the value of left operand is less than the
value of right operand, use <
5) If the value of left operand is greater or equal than 
the value of right operand, use >=
6) If the value of left operand is less or equal than 
the value of right operand, use <=

Let's make an example using functions and of course the 
comparison operators:

"""

#In the first comparison we are going to use equal or not equal

def compare_numbers (num_01,num_02):
    result = ''
    if num_01 == num_02:
        result = 'The numbers are equal'
    else:
        result = 'The numbers are not equal'
    return result

print(compare_numbers(31,31))
print(compare_numbers(12,1991))

#For the second comparison we will use greater o less

def compare_numbers_second (num_01,num_02):
    result = ''
    if num_01 > num_02:
        result = 'The first number is greater than the second'
    else:
        result = 'The first number is less than the second'
    return result

print(compare_numbers_second(17,32))
print(compare_numbers_second(108,55))

#For the last comparison we are going to use greater or equal, and less or equal

def compare_numbers_last(num_01,num_02):
    result = ''
    if num_01 >= num_02:
        result = 'The first number is greater or equal than the second'
    else:
        result = 'The first number is less than the second'
    return result

print(compare_numbers_last(18,18))
print(compare_numbers_last(1001,631))
print(compare_numbers_last(99,999))