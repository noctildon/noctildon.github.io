"""
A function defines a block of code that can be called from other code.
Functions are used to break down large, complex problems into smaller and
more manageable problems.
keywords: def, return, pass
"""

# define a function
def my_function():
    print("Hello from a function")

# call function
my_function()

# input arguments
def my_function_with_args(username, greeting):
    print(f"Hello, {username} , From My Function!, I wish you {greeting}")

my_function_with_args("John", "a great year!")


# default arguments and return value
def sum_two_numbers(a, b=10):
    return a + b

print(sum_two_numbers(1, 2))  # 3
print(sum_two_numbers(1))     # 11

# return multiple values
def sum_and_product(a, b):
    return a + b, a * b

sp = sum_and_product(2, 3)  # sp is (5, 6)
s, p = sum_and_product(5, 10)  # s is 15, p is 50

# lambda function
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)  # [4, 6, 8, 12]


# variable number of arguments
def sum_all_numbers(*args):
    total = 0
    for a in args:
        total += a
    return total

print(sum_all_numbers(1, 2, 3, 4, 5))  # 15

# variable number of keyword arguments

def print_all_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_all_key_values(name="John", age=23) # name = John


# pass keyword
def no_function():
    pass # do nothing, also works for loops and conditionals

no_function() # nothing happens
