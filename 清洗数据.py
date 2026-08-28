import pandas as pd
import numpy as np

# 制造含噪数据
data = {
    'Mouse_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3],  # 故意重复了2号和3号
    'Weight_g': [25.5, 30.1, '28.0kg', 24.3, 29.9, np.nan, 26.7, 31.2, 27.8, 25.0, 30.1, 28.0],
    'Blood_Pressure': [120, 118, 125, '异常', 122, 119, 121, 123, 124, 126, 118, 125],
    'Heart_Rate': [80, 85, 78, 82, 79, 81, np.nan, 84, 83, 86, 85, 78]
}

df = pd.DataFrame(data)
print("原始脏数据：")
print(df)

df_dropL = df.drop_duplicates()
print(df_dropL)

df_dropL['Weight_g'] = pd.to_numeric(df_dropL['Weight_g'], errors = 'coerce')
print(df_dropL)

df_dropL['Weight_g'] = df_dropL['Weight_g'].fillna(df_dropL['Weight_g'].mean())
print(df_dropL)

df_dropL['Blood_Pressure'] = df_dropL['Blood_Pressure'].replace('异常', np.nan)
df_dropL['Blood_Pressure'] = pd.to_numeric(df_dropL['Blood_Pressure'], errors= 'coerce')
df_dropL['Blood_Pressure'] = df_dropL['Blood_Pressure'].fillna(df_dropL['Blood_Pressure'].median())
df_dropL['Heart_Rate'] = df_dropL['Heart_Rate'].ffill()
df_dropL = df_dropL.reset_index(drop=True)
df_dropL['Weight_g'] = df_dropL['Weight_g'].astype(int)
df_dropL = df_dropL.drop_duplicates(subset=['Mouse_ID'], keep='last')
print(df_dropL)