import numpy as np


arr = np.array([45, 22, 19, 80,33])

# Replace all values < 30 with 0,else keep them

result = np.where(arr < 30,0, arr)

print("Original Array: ", arr)
print("Modified Array: ", result)