"""
Decorator is a function that takes another function as an argument and returns a function
The returned function is called wrapper function. It is used to modify the behavior of the original function
"""
import math
import time

def f1(x):
    print('f1:', x + 2)

def f2(x):
    print('f2:', x * 2)


f1(1)     # f1: 3
f2(1)     # f2: 2


"""
Now we want to modify the behavior of f1 and f2, eg. print HOWDY at the beginning
Firstly we define a decorator function
where input_func is the original function, wrapper add a few lines of code to input_func
"""

def decorator(input_func):
    def wrapper(x):
        print('HOWDY')
        input_func(x)
    return wrapper

@decorator
def f1_(x):
    print('f1:', x + 2)

@decorator
def f2_(x):
    print('f2:', x * 2)

f1_(1)  # HOWDY f1: 3
f2_(1)  # HOWDY f2: 2



"""
A useful example: print the execution time of a function
"""

# timer decorator
def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()

        timer_mesg = f'Function {func.__name__!r} executed in {(t2-t1):.4f}s'
        print(timer_mesg)
        return result
    return wrap_func


@timer
def f0():
    # calculate lots of factorials to simulate heavy computation
    print('f0 starts running...')
    for i in range(int(5e3)):
        math.factorial(i)
    print('f0 done')

f0()  # it took me around 1s
