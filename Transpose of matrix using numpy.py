import numpy as np
a = [1,2,3,4,5,6,7,8]
a = np.array(a)
a = a.reshape(2,4)
print("Matrix Before Transpose")
print(a)
a = a.transpose()
print("Matrix After Transpose")
print(a)
