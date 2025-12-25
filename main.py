import pandas as pd

print("Pandas DataFrame Example")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

print("\n")
df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

print("\n Only Age Column:")
print(df["Age"])

print("\nFiltered (Age > 28):")
print(df[df["Age"] > 28])