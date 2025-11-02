# model.py
from sklearn.linear_model import LinearRegression
import joblib

class HousePriceModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def predict(self, x_test):
        return self.model.predict(x_test)

    def save_model(self, path='house_price_model.pkl'):
        joblib.dump(self.model, path)

    def load_model(self, path='house_price_model.pkl'):
        self.model = joblib.load(path)