import pickle

import pandas as pd
import numpy as np
from pprint import pprint
import os


def train():
    path_to_dataset = os.path.join (os.path.dirname (__file__), 'Datasets/final_normalized.csv')
    dataset = pd.read_csv(path_to_dataset)
    dataset.head()

    X = dataset.iloc[:, 0:9].values
    y = dataset.iloc[:, 9].values

    from sklearn.model_selection import train_test_split

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    path_to_test_dataset = os.path.join (os.path.dirname (__file__), 'Datasets/SE_data.csv')
    test_dataset = pd.read_csv(path_to_test_dataset)
    X_test = test_dataset.iloc[:, 0:9].values
    y_test = test_dataset.iloc[:, 9].values



    # # Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    #
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)

    from sklearn.ensemble import RandomForestRegressor

    regressor = RandomForestRegressor(n_estimators=5, random_state=0)
    regressor.fit(X, y)

    # save the model here for future use
    pickle.dump(regressor, open('saved_rf_regressor.p', 'wb'))

    y_pred = regressor.predict(X_test)
    from sklearn import metrics

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    # Calculate the absolute errors
    errors = abs(y_pred- y_test)

    # Calculate mean absolute percentage error (MAPE)
    mape = 100 * (errors / y_test)

    # Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')


def predict(inputs):
    open_path = os.path.join(os.path.dirname(__file__), 'saved_rf_regressor.p')
    regressor = pickle.load(open(open_path,'rb'))
    return regressor.predict(inputs)

if __name__ == '__main__':
    train()