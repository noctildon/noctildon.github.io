"""
Python has GIL (Global Interpreter Lock) which means only one thread can be executed at a time
This script demonstrates how to use multiprocess to speed up the calculation of factorial by using multiple CPU cores
This only works for independent calculations, ie no shared variables or memory bewteen threads
You may need to install the packages: $pip3 install multiprocess filelock
"""

import multiprocess as mp
from math import factorial
from filelock import FileLock


def job(x):
    # calculate factorial x for demo
    a = factorial(x)
    b = factorial(x+1)
    r = b/a

    # save the result to a file
    with lock:
        with open(outputFile, 'a') as f:
            f.write(f'{x+1}!/{x}! = {r}\n')


def multicore():
    # crate a pool for the processes
    # using 4 cores
    pool = mp.Pool(processes=4)

    # 1st arg is the function
    # 2nd is the inputs of the function (use array to wrap multiple parameters)
    pool.map(job, range(100000)) # calculate 0! to 99999!


if __name__ == "__main__":
    global lock, outputFile

    outputFile = 'out.txt'   # the output file
    lock = FileLock(outputFile + '.lock')

    multicore()
