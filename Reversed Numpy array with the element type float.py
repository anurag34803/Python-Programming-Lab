import numpy as np
a = input("Enter Values\n").split()
a = np.array(a,dtype = np.float)
x = a[::-1]
print(x)
