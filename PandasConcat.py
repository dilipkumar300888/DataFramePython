import pandas as pd

df1 = pd.DataFrame({'A': [1,2], 'B': [3,4]})
df2 = pd.DataFrame({'A': [5,6], 'B': [7,8]})

concat_rows = pd.concat([df1,df2], axis=0)
print("\nRow-wise Concat:\n", concat_rows)

concat_cols = pd.concat([df1, df2], axis=1)
print("\nColumn-wise Concat:\n", concat_cols)