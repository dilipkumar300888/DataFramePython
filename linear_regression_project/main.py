from data import generate_data
from linear_regression_scratch import LinearRegressionScratch
from linear_regression_sklearn import LinearRegressionSklearn
from visualize import plot_results


# Load data
X, y = generate_data()

# Train scratch model
scratch_model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
scratch_model.fit(X, y)
y_pred_scratch = scratch_model.predict(X)

# Train sklearn model
sk_model = LinearRegressionSklearn()
sk_model.fit(X, y)
y_pred_sklearn = sk_model.predict(X)

# Print results
print(f"Scratch Model: y = {scratch_model.m:.3f}x + {scratch_model.c:.3f}")
print(f"Sklearn Model Coef: {sk_model.model.coef_[0]:.3f}, Intercept: {sk_model.model.intercept_:.3f}")

# Visualize comparison
plot_results(X, y, y_pred_scratch, y_pred_sklearn)