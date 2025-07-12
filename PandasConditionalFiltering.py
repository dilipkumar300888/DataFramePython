import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 35, 29],
    'Score': [85, 90, 78, 88, 92]
}


df = pd.DataFrame(data)

print("Original DataFrame:\n", df)