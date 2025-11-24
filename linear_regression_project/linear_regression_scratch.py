import numpy as np

class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, epochs=1000):
        print("\nInitializing LinearRegressionScratch model...\n")
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.m = 0
        self.c = 0

    def fit(self, X, y):
        n = float(len(X))
        print("\n this is Linear Regression from scratch\n fit function\n")
        for _ in range(self.epochs):
            y_pred = self.m * X + self.c
            D_m = (-2/n) * sum(X * (y - y_pred))
            D_c = (-2/n) * sum(y - y_pred)
            self.m -= self.learning_rate * D_m
            self.c -= self.learning_rate * D_c

    def predict(self, X):
        return self.m * X + self.c