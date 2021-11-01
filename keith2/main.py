import pandas as pd
import os
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

# files = [i for i in os.listdir("./Sales_Data")]
#
# all_months_data = pd.DataFrame()
#
# for i in files:
#     df = pd.read_csv("./Sales_Data/" + i)
#     all_months_data = pd.concat([all_months_data, df])
#
# all_months_data.to_csv("./Sales_Data/all_data.csv", index=False)

all_data = pd.read_csv("./Sales_Data/all_data.csv")

# print(all_data.info())

nan_df = all_data[all_data.isna().any(axis=1)]
# print(nan_df.head())

all_data.dropna(how='all', inplace=True)

# 'Or' error
# tempdf = all_data[all_data['Order Date'].str[0:2] == "Or"]
# print(tempdf.head())

all_data = all_data[all_data['Order Date'].str[0:2] != "Or"]

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = pd.to_numeric(all_data['Month'])
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Order ID'] = all_data['Order ID'].astype(int)

all_data['Sales'] = all_data["Quantity Ordered"] * all_data["Price Each"]


# best month for sales
# salesdf = all_data.groupby('Month').sum()
# .sort_values(by='Sales', ascending=False

# months = range(1, 13)
# plt.bar(months, salesdf['Sales'])
# plt.xticks(months)
# plt.ylabel("Sales in usd")
# plt.xlabel("Month numb")
# plt.show()

# city specific sales

def get_city(address):
    return address.split(', ')[1]


def get_state(address):
    return address.split(', ')[2].split(' ')[0]


# all_data[["Street", "City", "Post Code"]] = all_data["Purchase Address"].str.split(", ", expand=True)
# all_data["City"] = all_data["Purchase Address"].apply(lambda x: x.split(', ')[1] + " " + (x.split(', ')[2])[0:2])
# all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + " " + get_state(x))

# citysales = all_data.groupby('City').sum()
# print(citysales)

# cities = [i for i, mydf in all_data.groupby('City')]

# plt.bar(cities, citysales['Sales'])
# plt.xticks(cities, rotation='vertical', size=8)
# plt.ylabel("Sales in usd")
# plt.xlabel("City")
# plt.show()

# all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

# all_data['Hour'] = all_data['Order Date'].dt.hour
# all_data['Minute'] = all_data['Order Date'].dt.minute

# hours = [hour for hour, df in all_data.groupby('Hour')]
# hourlysales = all_data.groupby('Hour').sum()

# plt.plot(hours, hourlysales)
# plt.xticks(hours, size=8)
# plt.ylabel("Num of sales")
# plt.xlabel("hour")
# plt.show()

df = all_data[all_data['Order ID'].duplicated(keep=False)].copy()

df["Grouped"] = df.groupby('Order ID')['Product'].transform(lambda x: ', '.join(x))

df = df[['Order ID', 'Grouped']].drop_duplicates()

# from itertools import combinations
# from collections import Counter
# count = Counter()
# for row in df['Grouped']:
#     row_list = row.split(',')
#     count.update(Counter(combinations(row_list, 4)))
# print(df.head(20))
# for key, value in count.most_common(10):
#     print(key, value)

quantity_ordered = all_data.groupby('Product')['Quantity Ordered'].sum()
products = [product for product, i in all_data.groupby('Product')]

prices = all_data.groupby("Product")["Price Each"].mean()

print(prices)

# plt.bar(products, quantity_ordered)
# plt.xticks(products, rotation='vertical', size=8)
# plt.ylabel("quant")
# plt.xlabel("product")

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered)
ax2.plot(products, prices, 'k')

ax1.set_xticklabels(products, rotation='vertical', size=8)
ax1.set_xlabel('product name', size=8)
ax1.set_ylabel('Quantity ordered')
ax2.set_ylabel('price')

plt.show()

# test pull keith

