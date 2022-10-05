"""
Scipy is a collection of packages for scientific computing in Python
"""

from scipy import stats
from scipy import integrate
from scipy import interpolate
from scipy import optimize
from scipy import linalg
import numpy as np


# special functions
print(stats.gamma.pdf(0.5, a=2))  # gamma distribution
print(stats.norm.pdf(0.5, loc=0, scale=1))  # normal distribution


# integration
print(integrate.quad(lambda x: np.exp(-x), 0, 1))  # integrate exp(-x) from 0 to 1


# optimization
def f(x):
    return x ** 2 + 10 * np.sin(x)
res = optimize.minimize(f, x0=0)
print(res.x)  # minimum


# interpolation
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x ** 2 / 9.0)
f = interpolate.interp1d(x, y, kind='quadratic')
print(f(0.5))  # interpolate at 0.5


# linear algebra
a = np.array([[1, 2], [3, 4]])
print(linalg.inv(a))  # inverse of a matrix
print(linalg.det(a))  # determinant of a matrix
print(linalg.eig(a))  # eigenvalues and eigenvectors of a matrix
