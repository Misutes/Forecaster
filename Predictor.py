from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from DataFrame_org import learning_dataframe, future_days_columns


finally_dataframe = learning_dataframe()


def building_model(max_iter, hidden_layer_sizes):
    MLP = MLPRegressor(max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)
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


