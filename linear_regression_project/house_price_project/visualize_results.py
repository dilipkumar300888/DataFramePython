# Visualize_results.py
import matplotlib.pyplot as plt


def plot_actual_vs_predicted(y_true, y_pred):
    plt.scatter(y_true, y_pred, color='blue')
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], 'r--',label="Perfect Fit")
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.title('Actual vs Predicted House Prices')
    plt.legend()
    plt.show()