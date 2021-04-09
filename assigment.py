#!pip install numpy
from typing import no_type_check
import numpy as np

 # Initializing lists
#a=[0,1,2,3,4]
#b=[5,6,7,8,9]

#Problem 1
a = np.array([0,1, 2, 3,4])

b = np.array([5, 6,7,8,9])

arr = np.concatenate((a, b))

print(arr)


#Problem 2

c=[]
for i in range(0, len(a)):
   c.append(a[i] + b[i])


print(c)

#Problem 3
res=[]
d = np.ones(5, dtype = int)
for i in range(0, len(c)):
   res.append(c[i] + d[i])

print(res)