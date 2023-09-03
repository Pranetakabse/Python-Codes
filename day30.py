# -*- coding: utf-8 -*-
"""Day30.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fhiKXCWp7S3UeO4vrQWqcnFCzatB8Gqz

**Access 2-D Arrays**

Write a program to access the element on the first row, second column:
"""

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0, 1])

"""Write a program to access the element on the 2nd row, 5th column:
Output: 10
"""

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,4])

"""**Negative Indexing**

Write a Program to print the last element from the 2nd dim:
"""

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, -1])

"""Write a Program to print the last element from the 1st dim:
Output: 5

NumPy Array Slicing:

- We pass slice instead of index like this:
syntax: [start:end]

- We can also define the step:
syntax: [start:end:step]


-If we don't pass start index it will consider as 0
-If we don't pass end index it will consider till the end of the array.
-if we don't pass step it will consider as 1

Write a program to slice elements from index 1 to index 5 from the array:
"""

import numpy as np
arr = np.array([1 , 2, 3, 4, 5, 6, 7])
print(arr[1:5])

"""Write a program to slice the elements from index 4 to the end of the array:

Write a Program to slice from the index 3 from the end to index 1 from the end:
Output: [5,6]
"""

import numpy as np
arr = np.array([1 , 2, 3, 4, 5, 6, 7])
print(arr[-3: -1])

"""Write a program in which starting index is 1 and ending index is 5 with step 2."""