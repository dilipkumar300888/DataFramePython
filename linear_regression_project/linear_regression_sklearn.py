from sklearn.linear_model import LinearRegression
import numpy as np


class LinearRegressionSklearn:
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        X = X.reshape(-1, 1)  # Reshape for sklearn
        self.model.fit(X, y)

    def predict(self, X):
        X = X.reshape(-1, 1)  # Reshape for sklearn
        return self.model.predict(X)