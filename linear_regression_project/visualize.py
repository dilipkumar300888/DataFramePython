import matplotlib.pyplot as plt

def plot_results(X, y, y_pred_scratch, y_pred_sklearn):
    plt.scatter(X, y, color='blue', label='Actual data')
    plt.plot(X, y_pred_scratch, color='red', label='Scratch Model')
    plt.plot(X, y_pred_sklearn, color='green', linestyle='--', label='Sklearn Model')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression: Scratch vs Sklearn')
    plt.legend()
    print("\n ")
    plt.show()
    