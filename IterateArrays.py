import numpy as np

#Iterating 1D array
n=np.array([4,5,6,7,8,9])
for a in n:
    print(a)
print(f"Type = {type(n)}")
print(f"Data type = {n.dtype}")
print(f"Dimensions = {n.ndim}")
print("**********************")

#Iterating 2D array
p=np.array([[2,3],[8,9],[6,9]])
for b in p:
    print(b)
print(type(b))
print(b.dtype)
print(b.ndim)

#Iterating 3D array
s=np.array([[[4,5,6],[7,8,94]],[[4,3,5],[7,9,8]]])
for x in s:
    print(x)
print(type(x))
print(x.dtype)
print(x.ndim)
