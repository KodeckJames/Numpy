import numpy as np

#0D array
n=np.array(6)
print(n.ndim)
print(n.shape)
print("*****************")

#1D array
p=np.array([2,3,4,5])
print(p.ndim)
print(p.shape)

#2D array
q=np.array([[4,5,6,7],[9,4,2,5]])
print(q.ndim)
print(q.shape)

#3D array
r=np.array([[[8,3,6,4],[4,3,6,7],[9,7,6,3]]])
print(r)
print(r.ndim)
print(r.shape)
print("******************")

u=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[8,9,7],[6,4,3],[5,7,1]]])
print(u)
print(u.ndim)
print(u.shape)

#4D array
s=np.array([[[[2,3,4,5],[4,5,6,7],[6,2,3,7]]]])
print(s.ndim)
print(s.shape)