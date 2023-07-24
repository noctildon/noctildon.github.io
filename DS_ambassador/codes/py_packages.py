"""
Common used modules
  built-in: sys, os, time, math
  3rd party: numpy, matplotlib, pandas, scipy
  interactive: jupyter, ptpython

pip3 install numpy matplotlib pandas scipy jupyter ptpython
"""


import sys
import os
import time
import math


print(sys.version)   # python version
print(sys.path)      # accessiable paths
print(os.getcwd())   # current working directory
print(os.listdir())  # list files in current directory


ti = time.time()   # current time in seconds from 1970 (unix time), can be used to time a function
time.sleep(1)      # sleep for 1 second
tf = time.time()
print(tf - ti)     # time difference, should be around 1


print(math.pi)              # pi
print(math.sqrt(9))         # sqrt(9)
print(math.sin(math.pi/2))  # sin(pi/2), takes radians
print(math.log(10, 2))      # log2(10)
print(math.log10(10))       # log10(10)
print(math.log2(2))         # log2(2)
print(math.exp(-1))         # 1/e
print(math.factorial(5))    # 5!


sys.exit(0)  # exit the program and skip the rest of the code
