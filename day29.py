# -*- coding: utf-8 -*-
"""Day29.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15G6UGJ9000zfSWzbPFV0NhNfMxrBqo8D

**Numpy Module**
- NumPy is a Python library.
- NumPy is used for working with arrays.
- NumPy is short for "Numerical Python".

Create a NumPy array
"""

import numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

"""Checking NumPy Version:"""

import numpy as np
print(np.__version__)

"""Check the type of array"""

import numpy as np
arr = np.array([12, 13, 14, 15, 16])
print(arr)
print(type(arr))

"""Use a tuple to create a NumPy array:

Use of NumPy Library:
- Linear algebra
- Fourier Transform
- Matrices

0-D Arrays:
- 0-D arrays are the elements in an array. Each value in an array is a 0-D array.

Create a 0-D array with value 11
"""

import numpy as np

arr = np.array(11)
print(arr)

"""1-D arrays:
- An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
- These are the most common and basic arrays.

Create a 1-D array containing the values 11,22,33,44,55
"""

import numpy as np
arr = np.array([11, 22, 33, 44, 55])
print(arr)

"""2-D Arrays:
- An array that has 1-D arrays as its elements is called a 2-D array.
- These are often used to represent matrix.

Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

[[1 2 3]
 [4 5 6]]
"""

import numpy as np
arr = np.array([[1, 2,3], [4, 5, 6]])
print(arr)

"""Check Number of Dimensions

Check how many dimensions the arrays have:
"""

import numpy as np
a = np.array(65)
b = np.array([[23, 45, 34], [11, 23, 43]])
c = np.array([1, 2, 3, 4, 5])

print(a.ndim)
print(b.ndim)
print(c.ndim)

"""**NumPy Array Indexing**

Access Array Elements:
- The indexes in NumPy array start with 0, meaning that the first element has index 0, and the second has index 1 etc.

Get the first element from the array.
"""

import numpy as np
arr = np.array([12, 23, 23, 34])
print(arr[1])

"""Q.1) Write a Program which gets the second element from the array.

Q.2) Write a Program which gets the third and fourth elements from the array and add them.
"""