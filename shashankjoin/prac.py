import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)
# pd.set_option('display.max_rows', None)

data_import = pd.read_csv('data_cleaning_challenge.csv')

data_import = data_import.filter(regex='Row Type|Power1|Weight')
data_import = data_import[data_import["Power1"].notnull()]

print(data_import)