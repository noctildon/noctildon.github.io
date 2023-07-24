"""
Python has GIL (Global Interpreter Lock) which means only one thread can be executed at a time
This script demonstrates how to use multiprocess to speed up the calculation of factorial by using multiple CPU cores
This only works for independent calculations, ie no shared variables or memory bewteen threads
You may need to install the packages: $pip3 install multiprocess filelock
"""

import multiprocess as mp
from math import factorial
from filelock import FileLock
import time


def job(x):
    # calculate factorial x for demo
    a = factorial(x)
    b = factorial(x+1)
    result = b/a

    # save the result to a file
    with lock:
        with open(outputFile, 'a') as f:
            f.write(f'{x+1}!/{x}! = {result}\n')


def multicore():
    # crate a pool for the processes
    # using 4 cores
    pool = mp.Pool(processes=4)

    # 1st arg is the function
    # 2nd is the inputs of the function (use array to wrap multiple parameters)
    pool.map(job, range(10000)) # calculate 0! to 9999!


# memory sharing
def job_ms(v, num, l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num # use .value to get the value
        print(v.value)
    l.release()


def multicore_ms():
    # i for int, d for float
    # 2nd argu is the initial value
    v = mp.Value('i', 0) # initialize share variable
    l = mp.Lock() # initialize a lock

    p1 = mp.Process(target=job, args=(v, 1, l)) # pass the lock in
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    global lock, outputFile

    outputFile = 'out.txt'   # the output file
    lock = FileLock(outputFile + '.lock')

    multicore()
    # multicore_ms()
