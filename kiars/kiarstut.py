import pandas as pd
import numpy as np
import matplotlib as plt
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

# from funky import Summation

Example_Array1 = np.array([1, 2, 3])
Example_Array2 = np.array([4, 5, 6])
# print(Example_Array1 + Example_Array2)

Data_dictionary = {'First Column Data': [1, 3], 'Second Column Data': [2, 4]}

Example_df = pd.DataFrame(data=Data_dictionary)
print(Example_df)
# print(Example_df['First Column Data'][0:])

Data = np.array([Example_Array1, Example_Array2])
Second_Example_df = pd.DataFrame(data=Data, columns=['First Column Data', 'Second Column Data', 'Third Column Data'])
print(Second_Example_df)

Temp_df = Second_Example_df.set_index('First Column Data')
# print(Temp_df)
# print('\n')
# print(Temp_df.iloc[1, 0])
# print(Temp_df.loc[1, 'Third Column Data'])
# print(Example_df['Second Column Data'])
# print('\n')

# print(Example_df.join(Second_Example_df, lsuffix=' First', rsuffix='Second'))

mergedmofos1 = Example_df.merge(Second_Example_df, how='left')
mergedmofos2 = Example_df.merge(Second_Example_df, how='inner')
mergedmofos3 = Example_df.merge(Second_Example_df, how='right')
# print(mergedmofos1)
# print(mergedmofos2)
# print(mergedmofos3)

print(Second_Example_df.agg('mean', axis='rows')['Second Column Data'])
# summedcols = Second_Example_df.agg(func=Summation, axis='columns')

# .apply on individual cells
# print(Example_df.apply(lambda x:x*3))

# plotting
# print(Second_Example_df.plot(x='First Column Data', y='Third Column Data', kind='scatter'))
# plt.pyplot.show()

Larger_df = pd.DataFrame(data=np.random.randint(0, 10, size=(15, 5)), columns=['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5'])
# print(Larger_df)
# if not true/false
# print(Larger_df > 5)

# if not true = NaN
# print(Larger_df[Larger_df > 5])

# returns false
# print(Larger_df.mask(Larger_df > 8))

# to replace original:
# Larger_df.drop(columns=['Col 2', 'Col 5'], inplace=True)
# print(Larger_df)

# to create copy remove inplace=true
# Larger_df_shortened = Larger_df.drop(columns=['Col 1', 'Col 4'])
# print(Larger_df_shortened)

# Larger_testna = Larger_df.mask(Larger_df > 8).dropna(how='any', axis=0)
# print(Larger_testna)

print(Larger_df)

# replace certain vals with other
# dfreplace = Larger_df.replace(3, 11)

# fill
# dfreplace = Larger_df[Larger_df > 5].fillna('Nothing')
# print(dfreplace)

ax = Larger_df.reset_index().plot(x='index', y='Col 1', kind='scatter')
Larger_df.reset_index().plot(x='index', y='Col 2', kind='scatter', color='orange', ax=ax)
plt.pyplot.show()

