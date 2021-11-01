import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl as xl

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

# print(df.head(3))

df = pd.read_csv('pokemon_data.csv')

# df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(df[['Name', 'Attack', "Defense"][0:4]])

# print(df.head(4))

# print(df.iloc[2, 3])
#
# for index, row in df.iterrows():
#     print(index, row)

# print(df.loc[df['Type 1'] == "Fire"])

# print(df.describe())

# print(df.sort_values(["Type 1", "Generation"], ascending = [1,0] ))

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# cols = list(df.columns.values)

# df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Total'] <= 250)]

# new_df.to_csv('filtered.csv')

# print(new_df)

# print(df.loc[df["Type 1"].str.contains("Fire|Grass")])

# df.to_csv('modified.csv', index=False)

df = df.groupby(['Type 1']).mean().sort_values(["HP"], ascending=False)

print(df.columns)
print(df)
