import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)
print(arr.ndim)
print(arr.size)
print(arr.shape) # for rows and colums in case of 2D array and block rows and colums in case of 3D
print(arr.min())
print(arr.max())
print(arr.sum())
print(arr.sum(axis=0)) # axis 0 mean columns
print(arr.sum(axis=1 )) # axis 1 mean rows