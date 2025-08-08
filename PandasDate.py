import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01",periods=5,freq='D')
print(dates)

data = np.random.randint(100, size=5)
df = pd.DataFrame({'Date': dates, 'Value': data})
print(df)

df.set_index('Date', inplace=True)
print(df)
print(df.loc['2023-01-03'])