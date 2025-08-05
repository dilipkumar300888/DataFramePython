import pandas as pd

dates = pd.date_range(start="2023-01-01",periods=5,freq='D')
print(dates)