import pandas as pd
import os
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

cwd = str(os.getcwd())
files = [i for i in os.listdir(cwd + "/Sales_Data")]

# allmonthsdf = pd.DataFrame()
# for i in files:
#     df = pd.read_csv(cwd + "/Sales_Data/" + i)
#     allmonthsdf = pd.concat([allmonthsdf, df])
#
# allmonthsdf.to_csv(cwd + "/Sales_Data/allmonthsdfsec.csv", index=False)

df = pd.read_csv(cwd + "/Sales_Data/allmonthsdfsec.csv")

# rows with any nan
# print(df[df.isna().any(axis=1)])

df.dropna(axis=0, how='all', inplace=True)

df = df[df["Quantity Ordered"] != "Quantity Ordered"]

df["Month"] = df["Order Date"].str[0:2]
df["Month"] = pd.to_numeric(df["Month"])
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"])
df['Price Each'] = pd.to_numeric(df['Price Each'])

# best sales
df["Sales"] = df["Quantity Ordered"] * df['Price Each']
bestsales = df.groupby("Month").sum()
bestsales['Price Each'] = bestsales['Price Each']/bestsales['Quantity Ordered']
bestsales.reset_index(inplace=True)
# bestsales.sort_values("Sales", inplace=True)
# months = range(1, 13)
# plt.bar(months, bestsales['Sales'])
# plt.xticks(months)
# plt.ylabel("Sales in usd")
# plt.xlabel("Month numb")
# plt.show()
# print(bestsales)

df["City"] = df["Purchase Address"].str.split(", ", expand=True)[1]
df["State"] = (df["Purchase Address"].str.split(", ", expand=True)[2]).str.split(" ", expand=True)[0]
df["City + state"] = df["City"] + " " + df["State"]

citysales = df.groupby("City + state").sum().reset_index()
cities = [i for i, mydf in citysales.groupby('City + state')]
# plt.bar(cities, citysales['Sales'])
# plt.xticks(cities, rotation='vertical', size=8)
# plt.ylabel("Sales in usd")
# plt.xlabel("City")
# plt.show()


orderdf = df[df['Order ID'].duplicated(keep=False)].copy()

orderdf["Grouped"] = orderdf.groupby('Order ID')['Product'].transform(lambda x: ', '.join(x))

orderdf = orderdf[['Order ID', 'Grouped']].drop_duplicates()

from itertools import combinations
from collections import Counter

count = Counter()
for row in orderdf['Grouped']:
    row_list = row.split(', ')
    count.update(Counter(combinations(row_list, 4)))
# print(orderdf.head(20))
for key, value in count.most_common(10):
    print(key, value)



