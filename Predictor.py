from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt
from DataFrame_org import learning_dataframe, future_days_columns

finally_dataframe = learning_dataframe()


def machin_learning():
    MLP = MLPRegressor(max_iter=52, hidden_layer_sizes=117)
    X, Y = finally_dataframe[:2]
    MLP.fit(X, Y)
    return MLP


def visualization(ml_model):
    model = ml_model
    X_test, Y_test = finally_dataframe[2:]
    prediction = model.predict([X_test.iloc[0]])
    real_rates = Y_test.iloc[0]
    plt.plot(future_days_columns, prediction[0], label='prediction')
    plt.plot(future_days_columns, real_rates, label='real')
    plt.legend()
    plt.show()




visualization(machin_learning())
