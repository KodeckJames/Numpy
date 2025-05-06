#In NumPy, dimensions refer to the number of axes (or “levels”) in an array — they are often called axes or ranks or simply ndim (number of dimensions).

#NB: To understand this, just know that the nth dimension holds the arrays eg in 4-dimensional array, the 4th square bracket (dimension) holds the arrays.

import numpy as np
#1. 0-Dimensional Numpy array
n=np.array(25)
print("Dimension = ", n.ndim)

#2. 1-Dimensional Numpy array
p=np.array([10,20,30])
print("Dimension = ", p.ndim)

#3. 2-Dimensional Numpy array
o=np.array([[4,6,9],[7,8,9],[3,4,7]])
print("Dimensions =", o.ndim)
print(o)

#4. 3-Dimensional Numpy array
q=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[8,9,7],[6,4,3],[5,7,1]]])
print("Dimensions =", q.ndim)
print(q)

#5. 4-Dimensional Numpy array
r=np.array([[[[5,6,7],[8,9,10],[5,9,7]]]])
print("Dimensions =", r.ndim)
print(r)

