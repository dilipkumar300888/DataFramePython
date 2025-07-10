import pandas as pd


data = {
    'Product': ['A', 'B', 'C','D'],
    'Sales': [100, 200, 300, 400],
    'Discount': [10, 20, 5, 15]
}


df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Add a new column for net sales

df['Net_Sales'] = df['Sales'] - df['Discount']
print("\nWith Net Sales:\n", df)

# Summary statistics
print("\nDescribe numeric columns:\n", df.describe())

# Specific stats
print("Average Sales:", df['Sales'].mean())
print("Max Discount:", df['Discount'].max())