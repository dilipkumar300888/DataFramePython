import numpy as np

def generate_data():
    print("generate_data")
    # Sample data
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([3, 4, 2, 5, 6, 7, 8, 9])
    return X, y

def train_test_split(X, y, test_size=0.25):
    print("train test split")
    # Shuffle the data
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    X, y = X[indices], y[indices]
    
    # Split the data
    split_index = int(X.shape[0] * (1 - test_size))
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]
    
    return X_train, X_test, y_train, y_test