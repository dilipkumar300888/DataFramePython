import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class StockPricePredictor:
    def __init__(self, symbol='AAPL', period='2y'):
        """
        Initialize the stock price predictor
        
        Args:
            symbol (str): Stock symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            period (str): Time period for historical data ('1y', '2y', '5y', 'max')
        """
        self.symbol = symbol
        self.period = period
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None
        self.data = None
        self.features = None
        self.target = None
        
    def fetch_data(self):
        """Fetch historical stock data"""
        try:
            stock = yf.Ticker(self.symbol)
            self.data = stock.history(period=self.period)
            print(f"Successfully fetched {len(self.data)} days of data for {self.symbol}")
            return True
        except Exception as e:
            print(f"Error fetching data: {e}")
            return False
    
    def create_features(self, lookback_days=30):
        """
        Create features for machine learning model
        
        Args:
            lookback_days (int): Number of previous days to use as features
        """
        if self.data is None:
            print("No data available. Please fetch data first.")
            return False
        
        df = self.data.copy()
        
        # Calculate technical indicators
        df['SMA_10'] = df['Close'].rolling(window=10).mean()
        df['SMA_30'] = df['Close'].rolling(window=30).mean()
        df['EMA_12'] = df['Close'].ewm(span=12).mean()
        df['EMA_26'] = df['Close'].ewm(span=26).mean()
        
        # RSI calculation
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        df['MACD'] = df['EMA_12'] - df['EMA_26']
        df['MACD_signal'] = df['MACD'].ewm(span=9).mean()
        
        # Bollinger Bands
        df['BB_middle'] = df['Close'].rolling(window=20).mean()
        bb_std = df['Close'].rolling(window=20).std()
        df['BB_upper'] = df['BB_middle'] + (bb_std * 2)
        df['BB_lower'] = df['BB_middle'] - (bb_std * 2)
        df['BB_width'] = df['BB_upper'] - df['BB_lower']
        
        # Price change features
        df['Price_change'] = df['Close'].pct_change()
        df['Volume_change'] = df['Volume'].pct_change()
        df['High_Low_pct'] = (df['High'] - df['Low']) / df['Close']
        
        # Volatility
        df['Volatility'] = df['Price_change'].rolling(window=10).std()
        
        # Remove NaN values
        df = df.dropna()
        
        # Select feature columns
        feature_cols = ['Open', 'High', 'Low', 'Volume', 'SMA_10', 'SMA_30', 
                       'RSI', 'MACD', 'MACD_signal', 'BB_width', 'Price_change',
                       'Volume_change', 'High_Low_pct', 'Volatility']
        
        # Create sequences for time series prediction
        X, y = [], []
        for i in range(lookback_days, len(df)):
            X.append(df[feature_cols].iloc[i-lookback_days:i].values.flatten())
            y.append(df['Close'].iloc[i])
        
        self.features = np.array(X)
        self.target = np.array(y)
        self.feature_data = df
        
        print(f"Created {len(self.features)} samples with {self.features.shape[1]} features each")
        return True
    
    def train_model(self, model_type='random_forest', test_size=0.2):
        """
        Train the prediction model
        
        Args:
            model_type (str): Type of model ('linear', 'random_forest')
            test_size (float): Proportion of data for testing
        """
        if self.features is None or self.target is None:
            print("No features available. Please create features first.")
            return False
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.target, test_size=test_size, random_state=42, shuffle=False
        )
        
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Choose and train model
        if model_type == 'linear':
            self.model = LinearRegression()
        elif model_type == 'random_forest':
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        else:
            print("Unsupported model type. Using Random Forest.")
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        print(f"Training {model_type} model...")
        self.model.fit(X_train_scaled, y_train)
        
        # Make predictions on test set
        y_pred = self.model.predict(X_test_scaled)
        
        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"\nModel Performance:")
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"Mean Absolute Error: {mae:.4f}")
        print(f"R² Score: {r2:.4f}")
        
        # Store test results for plotting
        self.test_results = {
            'actual': y_test,
            'predicted': y_pred,
            'dates': self.feature_data.index[-len(y_test):]
        }
        
        return True
    
    def predict_future(self, days=30):
        """
        Predict future stock prices
        
        Args:
            days (int): Number of days to predict into the future
        """
        if self.model is None:
            print("No trained model available. Please train model first.")
            return None
        
        # Get the last sequence from the data
        last_sequence = self.features[-1].reshape(1, -1)
        last_sequence_scaled = self.scaler.transform(last_sequence)
        
        predictions = []
        current_sequence = last_sequence_scaled.copy()
        
        # Generate future predictions
        for _ in range(days):
            pred = self.model.predict(current_sequence)[0]
            predictions.append(pred)
            
            # Update sequence (simplified approach - in practice, you'd want to update with actual features)
            # This is a limitation of this approach for multi-step forecasting
            
        # Create future dates
        last_date = self.feature_data.index[-1]
        future_dates = [last_date + timedelta(days=i+1) for i in range(days)]
        
        return pd.DataFrame({
            'Date': future_dates,
            'Predicted_Price': predictions
        })
    
    def plot_results(self, show_future=True, future_days=30):
        """Plot historical data, test predictions, and future predictions"""
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Historical price and test predictions
        plt.subplot(2, 1, 1)
        plt.plot(self.feature_data.index, self.feature_data['Close'], 
                label='Historical Price', alpha=0.7)
        
        if hasattr(self, 'test_results'):
            plt.plot(self.test_results['dates'], self.test_results['actual'], 
                    label='Actual (Test)', color='green')
            plt.plot(self.test_results['dates'], self.test_results['predicted'], 
                    label='Predicted (Test)', color='red', linestyle='--')
        
        plt.title(f'{self.symbol} Stock Price Prediction - Historical & Test Results')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Future predictions
        if show_future:
            plt.subplot(2, 1, 2)
            
            # Show last 90 days of historical data for context
            recent_data = self.feature_data.tail(90)
            plt.plot(recent_data.index, recent_data['Close'], 
                    label='Recent Historical Price', color='blue')
            
            # Get future predictions
            future_pred = self.predict_future(future_days)
            if future_pred is not None:
                plt.plot(future_pred['Date'], future_pred['Predicted_Price'], 
                        label=f'Future Predictions ({future_days} days)', 
                        color='red', linestyle='--', marker='o', markersize=3)
            
            plt.title(f'{self.symbol} Future Price Predictions')
            plt.xlabel('Date')
            plt.ylabel('Price ($)')
            plt.legend()
            plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def get_prediction_summary(self, future_days=30):
        """Get a summary of predictions"""
        if self.model is None:
            return "No trained model available."
        
        current_price = self.feature_data['Close'].iloc[-1]
        future_pred = self.predict_future(future_days)
        
        if future_pred is not None:
            final_price = future_pred['Predicted_Price'].iloc[-1]
            price_change = final_price - current_price
            price_change_pct = (price_change / current_price) * 100
            
            summary = f"""
Prediction Summary for {self.symbol}:
Current Price: ${current_price:.2f}
Predicted Price in {future_days} days: ${final_price:.2f}
Expected Change: ${price_change:.2f} ({price_change_pct:+.2f}%)
            """
            return summary
        else:
            return "Could not generate predictions."

# Example usage
def main():
    # Initialize predictor
    predictor = StockPricePredictor(symbol='AAPL', period='2y')
    
    # Fetch data
    if predictor.fetch_data():
        # Create features
        if predictor.create_features(lookback_days=30):
            # Train model
            if predictor.train_model(model_type='random_forest'):
                # Show prediction summary
                print(predictor.get_prediction_summary(future_days=30))
                
                # Plot results
                predictor.plot_results(show_future=True, future_days=30)

if __name__ == "__main__":
    main()