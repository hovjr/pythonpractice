import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.array([
    ['a', 5, 9],
    ['b', 4, 61],
    ['c', 24, 9]]),
    columns=['name', 'attr11', 'attr12'])
df2 = pd.DataFrame(np.array([
    ['a', 5, 19],
    ['b', 14, 16],
    ['c', 4, 9]]),
    columns=['name', 'attr21', 'attr22'])
df3 = pd.DataFrame(np.array([
    ['a', 15, 49],
    ['b', 4, 36],
    ['c', 14, 9]]),
    columns=['name', 'attr31', 'attr32'])

df4 = pd.merge(pd.merge(df1, df2, on='name'), df3, on='name')

print(df4)

dfs = [df1, df2, df3]
dfs = [df.set_index('name') for df in dfs]
btest = dfs[0].join(dfs[1:])
print(btest)

print(btest.iloc[0, 1])
print(btest.loc['b', 'attr32'])