import numpy as np
import matplotlib.pyplot as plt

# Input (X) and Output (y) 
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 4, 2, 5, 6])


# Visualize the data
print("\n Visualizing the data...")
plt.scatter(X, y, color='blue', label='Actual data')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Study Hours vs Score')
plt.legend()
plt.show()