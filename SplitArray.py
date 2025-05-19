#Syntax:
#array_split(arr_name, split_num)
#split_num is the count of splits

#Splitting a 1D array
import numpy as np
n=np.array([2,3,4,5,6,7])
for a in n:
    print(a)
nsplit=np.array_split(n, 2)
for a in nsplit:
    print(a)

#Accessing a split 1D array :- Here you use the index number for the array element you want to display
print(f'Array1 = {nsplit[0]}')
print(f'Array2 = {nsplit[1]}')

#Splitting a 2D array:
p=np.array([[23,35,45,54],[68,79,80,95]])
psplit=np.array_split(p,2)
for a in psplit:
    print(a)
print(psplit[0])
print(psplit[1])