"""
Exception handling in Python
"""

try:
    print("Hello World")                     # try block
    raise Exception("This is an exception")  # manually raise an exception
except Exception as e:
    print("Exception: ", e)
finally:
    # always run
    print("This is the end")


try:
    print("Hello World" + 1)    # invalid operation
except Exception as e:
    print("Exception: ", e)


print('END of the program')
