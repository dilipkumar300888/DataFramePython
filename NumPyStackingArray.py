import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

v_stack = np.vstack((a,b))
print("\nVertical Stack:\n", v_stack)

h_stack = np.hstack((a,b))
print("\nHorizontal Stack:\n",h_stack)