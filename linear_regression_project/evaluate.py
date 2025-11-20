# evaluate.py

import numpy as np

def mean_absolute_error(y_true, y_pred):
    print("mean_absolute_error")
    return np.mean(np.abs(y_true - y_pred))

def mean_squared_error(y_true, y_pred):
    print("mean_squared_error")
    return np.mean((y_true - y_pred) ** 2)

def root_mean_squared_error(y_true, y_pred):
    print("root_mean_squared_error")
    return np.sqrt(mean_squared_error(y_true, y_pred))

def r2_score(y_true, y_pred):
    print("r2_score")
    ss_res= np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2