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

print(df)
print(bestsales)