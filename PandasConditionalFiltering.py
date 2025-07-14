import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 35, 29],
    'Score': [85, 90, 78, 88, 92]
}


df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Filter rows where Age is greater than 25
print("\nPeople older than 25:\n", df[df['Age'] > 25])

# Filter rows where Score is lesser than 80
print("\nPeople with Score less than 80:\n", df[df['Score'] < 80])

# Combine conditions using &
print("\nPeople older than 25 with Score greater than 80:\n", df[(df['Age'] > 25) & (df['Score'] > 80)])