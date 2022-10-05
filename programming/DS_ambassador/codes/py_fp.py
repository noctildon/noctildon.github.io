"""
Functional Programming
wrap everything in functions
decorator is a function that takes another function as an argument, adds some functionality and returns another function
"""
from time import time


def f1(x):
    return x**2


def f2(x, y):
    return x + y


# input a function, output a function
def my_decorator(func):
    # func: the input function
    # wrap_func: the output function = func + some functionality
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper


def say_whee():
    print("Whee!")


def testing_decorator():
    say_whee_ = my_decorator(say_whee)
    say_whee_()


# This function shows the execution time of the function object passed
def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()

        timer_mesg = f'Function {func.__name__!r} executed in {1e3*(t2-t1):.9f}ms'
        print(timer_mesg)
        return result
    return wrap_func


@timer_func
def main():
    a = f1(2)
    b = f1(5)
    c = f2(a, b)

    print(f'2^2+5^2={c}')


if __name__ == "__main__":
    main()
    print('-'*20)
    testing_decorator()