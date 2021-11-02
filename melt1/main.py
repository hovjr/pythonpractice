import pandas as pd
import os
import datetime
from datetime import datetime as dt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

pwd = os.getcwd()
# print(pwd)

filepath = pwd + "/datafilez/simple_csv.csv"

first_import = pd.read_csv(filepath, nrows=15)

shortened = first_import.loc[:, ['Column3']]

# print(first_import)
# print(shortened)


netflix = pd.read_csv('./datafilez/netflix_titles.csv')

# print(list(netflix.columns))
# print(netflix.describe())

# print(netflix["type"].unique())
# netflix[netflix["country"] == "Singapore"]

filter1 = netflix[(netflix['country'] == 'Singapore') | (netflix["rating"] == "TV-MA")]
# print(filter1)

netflix['computer_date'] = pd.to_datetime(netflix["date_added"])

# print(netflix['computer_date'])
# netflix.dropna(subset=["computer_date"], inplace=True)
# print(netflix)

netflix['computer_date'].fillna(dt(2020, 1, 1), inplace=True)

netflix[["Date Part 1", "Date Part 2"]] = netflix["date_added"].str.split(", ", expand=True)

netflix.rename(columns={"Date Part 2": "year"}, inplace=True)

netflix["cast"].fillna(value="no cast", inplace=True)

# nulldir = netflix.dropna(axis=0, subset=['director'])
# nulldir = netflix[netflix['director'].isnull()]

# print(netflix["director"].isnull())
# print(nulldir)

netflix["genre_count"] = netflix["listed_in"].map(lambda x: len(x.split(',')))

# print(netflix)
# print(netflix["genre_count"][1])

test4 = netflix.groupby(["country", "type"])["show_id"].count().reset_index()
# print(test4.sort_values(by="country"))

test3 = netflix.groupby(["country"])["show_id"].count().reset_index()
# print(test3.sort_values(by="country", ascending=True))

second_dataset = pd.read_csv("./datafilez/netflix_titles_second.csv")

new_dataset = pd.concat([netflix, second_dataset])

netflix_merged = pd.merge(left=new_dataset, right=test3, how="inner", on="country")

# print(netflix_merged.sort_values(by="country"))

pivtez = netflix.pivot_table(index="country",
                             columns="type",
                             values="title",
                             aggfunc='count',
                             fill_value=0
                             )
print(netflix)
print(pivtez)


