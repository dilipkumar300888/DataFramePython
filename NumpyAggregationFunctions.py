import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original array:\n", arr)

# Calculate the sum along the rows
print("\nRow-wise Sum:", np.sum(arr, axis=1))

# Calculate the mean along the columns
print("Column-wise Mean:", np.mean(arr, axis=0))