import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

df = pd.read_csv("./data_cleaning_challenge.csv")

# print(df.info())

# nonull = df[df['Unnamed: 10'].notnull()]
df.drop(columns=["Unnamed: 9", "Unnamed: 10"], inplace=True)
df.dropna(axis=0, how="all", inplace=True)

columnvalues = []
counter = 0
for i in df['Row Type']:
    if "first name" in i:
        counter += 1
    columnvalues.append(counter)

df['Iteration'] = columnvalues

df = df[df["Row Type"] != "Row Type"]

namedf = df[df["Row Type"].str.contains("first name")].copy()
namedf.drop(columns=["Speed1", "Speed2", "Electricity", "Effort", "Weight", "Torque"], inplace=True)
namedf.rename(columns={"Row Type": "First Name", "Iter Number": "Last Name", "Power1": "Date"}, inplace=True)

namedf["First Name"] = namedf["First Name"].str[12:]
namedf["Last Name"] = namedf["Last Name"].str[11:]
namedf["Date"] = namedf["Date"].str[6:]

nonaydf = df[~(df["Row Type"].str.contains("first name"))]

cleanfinal = pd.merge(left=namedf, right=nonaydf, on="Iteration", how="inner")
cleanfinal.drop(columns='Iteration', inplace=True)

cleanfinal.to_csv("second_try.csv", index=False)

# print(cleanfinal)
