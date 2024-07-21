import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\Dell\OneDrive\Desktop\python project\worldometer_data.csv',encoding='unicode_escape')
print(df.shape)
# print(pd.isnull(df).sum())
# print(df.dropna(inplace=True))

