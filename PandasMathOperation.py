import pandas as pd


data = {
    'Product': ['A', 'B', 'C','D'],
    'Sales': [100, 200, 300, 400],
    'Discount': [10, 20, 5, 15]
}


df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Add a new column for net sales