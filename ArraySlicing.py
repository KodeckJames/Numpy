import numpy as np

#Slicing arrays syntax:
#arr[start:end] start is included but end is excluded
n=np.array([4,2,5,6,4,7,0,3,2,1])
print(n[1:4])   
print(n[2:])   
print(n[:4])   

#Slicing one-dimensional arrays with step
#Syntax: arr[start:end:step]
print(n[0:9:2])

#Slicing a 2D array
p=np.array([[2,3,4,5],[5,6,7,8],[2,3,6,9]])
print(p[2,0:3])

#Slicing for both in a 2D array
p=np.array([[2,3,4,5],
            [5,6,7,8],
            [2,3,6,9]])
print(p[0:3, 1:3])

#✅ Understanding the slice p[0:3, 1:3]
#0:3 → rows from index 0 up to (but not including) 3 → rows 0, 1, 2
#1:3 → columns from index 1 up to (but not including) 3 → columns 1, 2
