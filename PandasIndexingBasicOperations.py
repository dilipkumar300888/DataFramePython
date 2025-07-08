import pandas as pd

data = {
    'Name' : ['Alice','Bob','Charlie'],
    'Age' : [25, 30, 35],
    'Salary' : [50000, 60000, 70000]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n",df)

# Accessing a single column
print("\nAccessing 'Age' column :\n", df['Age'])

# Access a row by index
print("\nAccessing row at index 1:\n", df.iloc[1])

# Access a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame after adding 'Bonus' column:\n", df)

# Filter rows
print("\nPeople with Salary greater than 55000:\n", df[df['Salary'] > 55000])