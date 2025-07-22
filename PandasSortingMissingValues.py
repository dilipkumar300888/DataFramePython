import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, np.nan, 78, 88, 92],
    'Age': [24, 30, 22, np.nan, 29]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Sort by Score (ascending)
print("\nDataFrame sorted by Score:\n", df.sort_values(by='Score'))


# Drop rows with missing values
print("\nDrop rows with any missing values:\n", df.dropna())


# Fill missing values
df_filled = df.fillna({'Score': 0, 'Age': df['Age'].mean()})

print("\nFilled missing values:\n", df_filled)


# Check for nulls
print("\nWhere Score is missing:\n", df[df['Score'].isnull()])



df['Result'] = np.where(df['Score'] >= 80, 'Pass', 'Fail')


print("\nDataFrame with Result column:\n", df)

median_age = df['Age'].median()

print("\nMedian Age:", median_age)

df_cleaned = df.dropna(subset=['Score', 'Age'], how='all')
print("\nAfter Dropping Rows with both Score and Age missing:\n", df_cleaned)