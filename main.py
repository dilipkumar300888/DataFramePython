import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

print("\n Only Age Column:")
print(df["Age"])

print("\nFiltered (Age > 28):")
print(df[df["Age"] > 28])