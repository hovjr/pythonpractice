import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

pew = pd.read_csv('./data/pew.csv')

pew_long = pd.melt(pew, id_vars='religion',
                   var_name='income',
                   value_name='count'
                   )


# print(pew)
# print(pew_long.head())

billboard = pd.read_csv('./data/billboard.csv')
# print(billboard.head())
billboard_melt = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week',
                         value_name='rating'
                         )
# print(billboard_melt.head())

# Splitting long data
ebola = pd.read_csv('./data/country_timeseries.csv')

ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])

# split variable by _ turns into array, get 0,1 type or death
# variable_split = ebola_long['variable'].str.split('_')
# print(variable_split.str.get(0))
#
# ebola_long['stats'], ebola_long['country'] = [variable_split.str.get(0), variable_split.str.get(1)]
#
# ebola_long.drop(columns='variable', inplace=True)


# shorter
ebola_long[['stats_e', 'country_e']] = ebola_long['variable'].str.split('_', expand=True)

# print(ebola_long.head())

# opposite of melt convert to columns
weather = pd.read_csv('./data/weather.csv')

weather_melt = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'],
                       var_name='day',
                       value_name='temp'
                       )

# pivot
weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day'],
    columns='element',
    values='temp'
)

weather_tidy.reset_index(inplace=True)

# print(weather_melt)
# print(weather_tidy.head())


# multiple types of obs units in same table

# print(billboard_melt.loc[billboard_melt['track'] == 'Loser'])

songs_only = billboard_melt[['year', 'artist', 'track', 'time']].drop_duplicates()

# print(billboard_melt.head())
songs_only['id'] = range(len(songs_only))

# will just give songs an id
billboard_ratings = billboard_melt.merge(
    songs_only, on=['year', 'artist', 'track', 'time']
)

print(billboard_ratings)