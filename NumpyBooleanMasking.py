import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])

# Create a mask for elements greater than 30
mask = arr > 30
print("Mask: ", mask)


# Use mask to filter
print("Filtered Elements (arr > 30): ", arr[mask])


