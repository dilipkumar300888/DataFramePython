# run.py

from preprocess import load_and_preprocess_data
from model import HousePriceModel
from evaluate_model import evaluate_model
from visualize_results import plot_actual_vs_predicted

# Step 1: Load and preprocess data
X_train, X_test, y_train, y_test = load_and_preprocess_data(
    r"D:\PythonProjects\Dataframe\linear_regression_project\house_price_project\data\house_data.csv"
)

# Step 2: Initialize and train the model
model = HousePriceModel()
model.train(X_train, y_train)

# Step 3: Make predictions
y_pred = model.predict(X_test)

# Step 4: Evaluate the model
mae, rmse, r2 = evaluate_model(y_test, y_pred)

# Step 5: Visualize the results
plot_actual_vs_predicted(y_test, y_pred)

# Step 6: Save model
model.save_model('house_price_model.pkl')
print("\n Model training complete and model saved as 'house_price_model.pkl'")