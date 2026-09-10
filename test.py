import pandas as pd
import csv
import os

df_1 = pd.read_csv("old.csv")
df_2 = pd.read_csv("new.csv")
print("========================old_dev========================")
print(df_1)
clean_old_dev = df_1.drop_duplicates(keep="first")
if df_1.duplicated().any():
    print("========================clean_old_dev========================")
    print(clean_old_dev)
else:
    print("无重复内容！")

print("========================new_dev========================")
print(df_2)
clean_new_dev = df_2.drop_duplicates(keep="first")
if df_2.duplicated().any():
    print("========================new_dev========================")
    print(clean_new_dev)
else:
    print("无重复内容！")