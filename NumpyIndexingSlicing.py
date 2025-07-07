import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)
print("First Element:", arr[0])
print("Last Two Elements:", arr[-2:])
print("Every Second Element:", arr[::2])


mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:\n", mat)
print("Element at 2nd row, 3rd column:", mat[1][2])
print("First two rows:", mat[:2])
print("Last column:\n", mat[:, -1])