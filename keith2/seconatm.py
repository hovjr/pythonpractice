import pandas as pd
import os

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

cwd = str(os.getcwd())
files = [i for i in os.listdir(cwd + "/Sales_Data")]
print(files)
allmonthsdf = pd.DataFrame()

for i in files:
    df = pd.read_csv(cwd + "/Sales_Data/" + i)
    allmonthsdf = pd.concat([allmonthsdf, df])

allmonthsdf.to_csv(cwd + "/Sales_Data/allmonthsdfsec.csv", index=False)

print(allmonthsdf)

