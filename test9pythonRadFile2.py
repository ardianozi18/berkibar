# code here
import pandas as pd

df_csv = pd.read_csv("diamonds-1.csv")

print(df_csv["price"].mean())
print(df_csv["depth"].std())
print(df_csv["carat"].max())