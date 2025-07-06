import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
    }

# Create a DataFrame
df = pd.DataFrame(data)

print("DataFrame:")
print(df)