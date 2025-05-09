import numpy as np

#Accessing elements from a 1D array
n=np.array([2,3,4])
print(type(n))
print(n[0])
print(n[2])

#Accessing elements from a 2D array
p=np.array([[4,5,6,9],[5,3,5,6]])
print(p[1])
print(p[1,0])
print(p[1,1])
print(p[1,2])
print(p[1,3])

#Accessing elements from a 3D array
r=np.array([[[2,3,4],[4,7,8]],[[5,0,9],[4,3,1]]])
print(r.ndim)
print(r[1,1,2])

#Accessing the last element from a 1D array with negative indexing
q=np.array([3,4,5])
print(q[-1])

#FOR THE OTHERS IT'S JUST THE SAME CONCEPT
