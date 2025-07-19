import numpy as np

arr = np.array([50,20,90,15,70])

#Replace values < 40 with 0, others stay the same
new_arr = np.where(arr < 40, 0, arr)

print("Original array:", arr)
print("Modified array:", new_arr)