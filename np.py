import numpy as np
import pandas as pd

data = {
    'A':[21, np.nan, 22, 4, np.nan],
    'B':[31, 32, 33, 34, 35],
    'C':[np.nan, np.nan, np.nan, np.nan, np.nan],
    'D':[46, 47,np.nan, 48, 49]
}

df = pd.DataFrame(data)

def count_nan(df):
    return df.isna().sum().sum()

print(count_nan(df))

# df_bfill = df.bfill()
# print(df_bfill)

# df_ffill = df.ffill()
# print(df_ffill)

# df_fill_0 = df.fillna(0)
# print(df_fill_0)