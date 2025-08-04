import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

v_stack = np.vstack((a,b))
print("\nVertical Stack:\n", v_stack)

h_stack = np.hstack((a,b))
print("\nHorizontal Stack:\n",h_stack)

c = np.array([[1,2,3,4],[5,6,7,8]])
d = np.array([[9,10,11,12],[13,14,15,16]])

v_stack_2d = np.vstack((c,d))
print("\nVertical Stack 2d:\n",v_stack_2d)

h_stack_2d = np.hstack((c,d))
print("\nHorizontal Stack 2d:\n",h_stack_2d)