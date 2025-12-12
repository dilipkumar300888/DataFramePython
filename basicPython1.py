import numpy as np

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 2, 5, 6])

# Initialize parameters
print("\n Training a simple linear regression model using Gradient Descent...")
m = 0  # slope
c = 0  # intercept
L = 0.01  # learning rate
epochs = 1000  # number of iterations
n = float(len(X))  # number of data points

# Gradient Descent Algorithm
for i in range(epochs):
    print(f"Iteration {i+1}: m = {m:.4f}, c = {c:.4f}")
    y_pred = m * X + c  # predicted y
    D_m = (-2/n) * sum(X * (y - y_pred))  # derivative w.r.t m
    D_c = (-2/n) * sum(y - y_pred)  # derivative w.r.t c
    m = m - L * D_m  # update m
    c = c - L * D_c  # update c

print(f"After {epochs} iterations:\nm = {m:.4f}, c = {c:.4f}")