import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# print(df.columns)
# print(df.index)
# print(df.shape)
# print(type(df))
# print(df.values)

# check for missing data
print(df.info())

country_df = df['country']
# print(type(country_df))

print(df.loc[df['year'] == 1967, ['year', 'pop']])