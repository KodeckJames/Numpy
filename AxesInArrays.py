import numpy as np

#Get minimum value with axes in Numpy
n=np.array([[8,6,3,2],[9,7,5,3],[2,3,4,5]])
for a in n:
    print(a)

#Minimum value
print(n.min()) 

#Minimum value with axis 0 (vertical axes)
print(n.min(axis=0))

#Minimum value with axis 1 (horizontal axes)
print(n.min(axis=1))