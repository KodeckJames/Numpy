import numpy as np

#Reshaping 1D to 2D array
n=np.array([1,2,3,4,5,6])
q=n.reshape(2,3)
print(q)
print(q.shape)

#Reshaping 3D array to 1D array (Flattening the array)
p=np.array([[[3,4,5,6],[7,8,9,0]]])
s=p.reshape(-1)
print(s)