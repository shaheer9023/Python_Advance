import numpy as np
n=int(input("enter number of elemenys : "))
data=[]
for i in range(n):
    element=int(input("enter elements : "))
    data.append(element)
array=np.array(data)
print(array)
array
print(np.ndim(array)) # dimention