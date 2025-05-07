import numpy as np

#With integers 
n=np.array([10,30,50])
print(n.dtype)

#With strings
p=np.array(["JJ","JJOndix","Concatenate"])
print(p.dtype)
# U = Unicode string
# 11 = Maximum characters input

#Set the datatype size within a numpy array
q=np.array(["rubix","cube","chess"], dtype="S9")
print(q.dtype)

#Converting one datatype to another
#Use the astype() method to do that
r=np.array([15,18,30,49])
print(r)
print(r.dtype)

s=r.astype("i")
print(s)
print(s.dtype)