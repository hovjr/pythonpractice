import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

df = pd.read_csv("./data_cleaning_challenge.csv")


# print(df.info())
# print(df.head(20))

nonull = [df["Unnamed: 10"].notnull()]
print(nonull)