import pandas as pd
import numpy as np
import matplotlib as plt
import datetime
from datetime import datetime as dt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

Running_df = pd.read_csv('Running.csv')
Cycling_df = pd.read_csv('Cycling.csv')
Walking_df = pd.read_csv('Walking.csv')
Weights_df = pd.read_csv('Weights.csv')

Activity_DataFrames = [Running_df, Cycling_df, Walking_df, Weights_df]

# import certain columns
# running_datetime = pd.read_csv('Running.csv', usecols=lambda x:x in ['Date', 'Distance', 'Moving Time'])
# print(Running_df.head(10))

# running_datetime = running_datetime.set_index('Date')
# print(running_datetime)
# print(running_datetime.iloc[0]['Distance'])

# skiprows same as usecols but rows to skip
# dtype to specify what datatypes to be used only works if consistent data in columns
# nrows which rows to read

Running_df.drop(columns=['Activity Type', 'Favorite', 'Min Temp', 'Max Temp', 'Surface Interval',
                         'Decompression', 'Grit', 'Flow', 'Dive Time', 'Training Stress Score®',
                         'Avg Vertical Ratio', 'Avg Vertical Oscillation', 'Min Elevation', 'Max Elevation',
                         'Number of Laps'], inplace=True)
# print(Running_df.columns.values)


Example_date = Running_df['Date'][0]
# print(Example_date)
# print((Running_df.dtypes['Date']))

# print(dt.strptime(Example_date, "%Y-%m-%d %H:%M:%S"))

Running_df['Date'] = Running_df['Date'].apply(dt.strptime, args=("%Y-%m-%d %H:%M:%S",))

Running_df = Running_df[Running_df['Avg HR']!='--']
Running_df = Running_df.astype({'Avg HR':'int'})

# Running_df['Avg Pace'] = Running_df['Avg Pace'].apply(dt.strptime, args=('%M:%S',))
# Temp_df = Running_df[Running_df['Avg Pace'] < dt.strptime('5:35', '%M:%S')]
# Temp_df = Temp_df[Temp_df['Avg Pace'] > dt.strptime('5:25', '%M:%S')]
# Temp_df = Temp_df[Temp_df['Date'] > dt.strptime('2021-06', '%Y-%m')]
# Running_df.reset_index()

# Temp_df.sort_values('Avg Pace', ascending=True)
# Temp_df = Temp_df.reset_index()
# .drop(columns='blabal') to drop index column ie
# print(Temp_df)

# Temp_df.plot(x='Date', y='Avg HR', kind='scatter', color='orange')

Running_df['Date'] = Running_df['Date'].apply(dt.strftime, args=('%b-%y',))
Running_df = Running_df[['Date', 'Avg HR']].groupby(['Date'], sort=False, as_index=False).mean()
# Running_df = Running_df.reset_index()
# same as as_index=False

print(Running_df)

# Total_Dist_df = Running_df[['Date', 'Distance']].groupby(['Date'], sort=False, as_index=False).sum()
# print(Total_Dist_df)
# print(Running_df.dtypes['Avg HR'])

Running_df[::-1].plot(x='Date', y='Avg HR', color='orange')
# Total_Dist_df[::-1].plot(x='Date', y='Distance', color='orange')

plt.pyplot.show()

