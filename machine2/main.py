import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)

housing_data = pd.read_csv('./data/Chapter 2 - housing.csv')

# housing_data["ocean_proximity"].value_counts().plot(kind='barh')
# plt.show()

housing_data['income_cat'] = pd.cut(housing_data['median_income'],
                                    bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                    labels=[1, 2, 3, 4, 5]
                                    )
# housing_data["income_cat"].hist()
# plt.show()

y = housing_data["median_house_value"]
X = housing_data.drop("median_house_value", axis=1)

# housing_data.hist(bins=50)
# plt.show()

# split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)



print(housing_data.corr())
