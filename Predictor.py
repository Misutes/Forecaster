from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from DataFrame_org import learning_dataframe, days_columns


finally_dataframe = learning_dataframe()


def building_model(max_iter, hidden_layer_sizes):
    MLP = MLPRegressor(max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes, random_state=42)
    x_train, y_train = finally_dataframe[:2]
    MLP.fit(x_train, y_train)
    return MLP


def visualization(network):
    model = network
    x_test, y_test = finally_dataframe[2:]
    prediction = model.predict([x_test[2]])
    real_rates = y_test[2]
    plt.plot(real_rates, label='real')
    plt.plot(prediction[0], label='prediction')
    plt.legend()
    plt.show()


visualization(building_model(177, 242))