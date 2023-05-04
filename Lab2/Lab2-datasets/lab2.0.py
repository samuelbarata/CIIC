import numpy as np
x = np.array([1, 2, 3])
print(x)
y = np.arange(10) # like Python's range, but returns an array
print(y)
a = np.linspace(0, 2, 4)
b = np.linspace(0, 2, 4) # create an array with four equally
c = a + b
print(c)
print(a**2)

a = np.linspace(-np.pi, np.pi, 100)
b = np.sin(a)
c = np.cos(a)

from numpy.random import rand
from numpy.linalg import solve, inv
a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
a.transpose()
inv(a)
b = np.array([3, 2, 1])
solve(a, b) # solve the equation ax = b
c = rand(3, 3) * 20 # create a 3x3 random matrix of values within
c
np.dot(a, c) # matrix multiplication
a @ c # Starting with Python 3.5 and NumPy 1.10
