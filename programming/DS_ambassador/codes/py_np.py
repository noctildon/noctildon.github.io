"""
Numpy is a library for the python, adding support for large,
multi-dimensional arrays and matrices, along with a large collection of high-level
mathematical functions to operate on these arrays.

pip install numpy
"""

import numpy as np


# numpy 1d array (vector)
a = np.array([1, 2, 3, 4, 5])  # the elements must be the same type
print(a)
print(a.shape)       # shape of the array
print(a[0])          # first element
print(a[::-1])       # reverse the array
print(a + 1)         # add 1 to each element
print(a * 2)         # multiply each element by 2
print(a ** 2)        # square each element
print(a + a)         # add two arrays (element-wise)
print(a * a)         # multiply two arrays (element-wise)
print(a @ a)         # dot product of two arrays
print(a.dot(a))      # dot product of two arrays
print(a.sum())       # sum of all elements
print(a.mean())      # mean of all elements
print(a.std())       # standard deviation of all elements
print(a.min())       # minimum of all elements
print(a.max())       # maximum of all elements
a = np.append(a, 6)  # append 6 to the end of the array
print(a)             # [1 2 3 4 5 6]


# apply function to each element
def f(x):
    return x ** 2

# if f is too complicated, this may fail
print(f(a)) # [ 1  4  9  16  25  36]

# slightly slower than the above, but more flexible and reliable
print(np.array([f(x) for x in a]))  # [ 1  4  9  16  25  36]


# numpy 2d array (matrix)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)   # shape of the array
print(a[0, 0])   # first element
print(a[0, :])   # first row
print(a[:, 0])   # first column
