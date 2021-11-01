import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)


data = pd.read_csv('./student/student-mat.csv', delimiter=';')

data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

predict = data["G3"]

X = np.array(data.drop("G3", 1))
y = np.array(data["G3"])

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(X_train, y_train)
acc = linear.score(X_test, y_test)
print(acc)

print('Coefficient: ', linear.coef_)
print('Intercept: ',  linear.intercept_)

predictions = linear.predict(X_test)

for x in range(len(predictions)):
    print(predictions[x], X_test[x], y_test[x])

