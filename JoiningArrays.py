import numpy as np

#We use: concatenate() method: Joining along with axis, unlike keys in SQL ... stack methods: Joining along a new axis, unlike keys in SQL

n1=np.array([5,10,15,20])
n2=np.array([25,30,35,40])

print("Iterating array 1")
for a in n1:
    print(a)

print("Iterating array 2")
for a in n2:
    print(a)

resarr=np.concatenate((n1,n2))
print(f"After joining = {resarr}")


 #Joining using Stack Methods:
 #stack(), hstack(), vstack(), dstack(), column_stack()
 # 1. stack()
stackArr=np.stack((n1,n2), axis=1)
print(f'After joining = \n {stackArr}')

#Joining along rows using hstack()
hstackArr=np.hstack((n1,n2))
print(f"\nAfter joining along rows = \n{hstackArr}")

#Joining along columns using vstack()
vstackArr=np.vstack((n1,n2))
print(f"After joining along columns = \n {vstackArr}")

#Joining along columns using dstack()
dstackArr=np.dstack((n1,n2))
print(f"After joining along depth = \n {dstackArr}")

#Joining along columns using dstack()
colstackArr=np.column_stack((n1,n2))
print(f"After joining along depth = \n {colstackArr}")
