import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)
# pd.set_option('display.max_rows', None)

data_import = pd.read_csv('data_cleaning_challenge.csv')
data_import.drop(columns=['Unnamed: 9', 'Unnamed: 10'], inplace=True)

data_import.dropna(how='all', axis=0, inplace=True)

# print(data_import.iloc[0]["Row Type"])

# print(data_import.iloc[0]["Row Type"] == "first name: Person")

# for i in data_import["Row Type"]:
#     if "first name" in i:
#         data_import.drop(i, axis=0, inplace=True)

column_values = []
counter = 0
for i in data_import["Row Type"]:
    if "first name" in i:
        counter += 1
    column_values.append(counter)

data_import = data_import
data_import["Iteration"] = column_values

data_import = data_import[data_import["Row Type"] != "Row Type"]
name_df = data_import[data_import["Row Type"].str.contains("first name:")]
name_df.drop(columns=["Speed1", "Speed2", "Electricity", "Effort", "Weight", "Torque"], inplace=True)
name_df.rename(columns={"Row Type": "First Name", "Iter Number": "Last Name", "Power1": "Date"}, inplace=True)

name_df["First Name"] = name_df["First Name"].str[12:]
name_df["Last Name"] = name_df["Last Name"].str[11:]
name_df["Date"] = name_df["Date"].str[6:]

noname_df = data_import[~data_import["Row Type"].str.contains("first name:")]

cleandf = pd.merge(left=name_df, right=noname_df, how="inner", on="Iteration")
cleandf.drop(columns=["Iteration"], inplace=True)
# to drop row eg first total:
# cleandf.drop([8], axis=0, inplace=True)
print(cleandf.head(50))

print("test push")
print("eat shit")

cleandf.to_csv("Clean_Df.csv", index=False)
