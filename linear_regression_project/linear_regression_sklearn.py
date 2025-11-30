from sklearn.linear_model import LinearRegression
import numpy as np


class LinearRegressionSklearn:
    def __init__(self):
        print("Initializing LinearRegressionSklearn model...\n")
        self.model = LinearRegression()

    def fit(self, X, y):
        print("Linear Regression using sklearn\n fit function\n")
        X = X.reshape(-1, 1)  # Reshape for sklearn
        self.model.fit(X, y)

    def predict(self, X):
        print("Linear Regression using sklearn\n predict function\n")
        X = X.reshape(-1, 1)  # Reshape for sklearn
        return self.model.predict(X)