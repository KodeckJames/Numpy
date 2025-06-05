import numpy as np

#Finding intersection between 2 arrays:
n=np.array([[2,3,4,5],[6,7,4,2]])
p=np.array([[6,7,8,2],[2,3,7,8]])
print(np.intersect1d(n,p))

#NB:- If no elements are identical, it returns an empty array