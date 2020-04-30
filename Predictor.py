from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from DataFrame_org import *


def machin_learning(dataframe):
    MLP = MLPRegressor()
    X, Y = dataframe[:2]
    MLP.fit(X, Y)
    return MLP


def visualization():
    model = machin_learning(dataframe_formation(learning_date()))
    X_test, Y_test = dataframe_formation(learning_date())[2:]
    prediction = model.predict(X_test.head(1))
    real_rates = Y_test.iloc[0]
    plt.plot(future_days_columns, prediction[0], label='prediction')
    plt.plot(future_days_columns, real_rates, label='real')
    plt.legend()
    plt.show()


visualization()
