import numpy as np
print(np.ones((5,5),dtype=int))
print("*"*50)
print(np.ones((5,5),dtype=[('x','int'),('y','bool')]))