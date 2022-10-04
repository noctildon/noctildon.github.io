"""
Variable scope in python
Keyword: global
"""

# scope
x = 1
def f():
    x = 2 # local scope, won't overwrite the global x
    print(x)

f()       # 2
print(x)  # 1


# global variable
y = 1
def g():
    global y  # declare y as global variable
    y = 2     # overwrite the global y
    print(y)

g()       # 2
print(y)  # 2
