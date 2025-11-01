import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Separate features and target variable
    x = df.drop(columns=['Price ($ in lakhs)'])  # Drop target column for preprocessing
    y = df['Price ($ in lakhs)']

    # Normalize the features
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # Split the dataset into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

    return x_train, x_test, y_train.values, y_test.values, scaler