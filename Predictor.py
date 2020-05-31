from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from DataFrame_org import learning_dataframe

finally_dataframe = learning_dataframe()


# creating and training model
def building_model(max_iter, hidden_layer_sizes):
    MLP = MLPRegressor(max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes, random_state=42)
    x_train, y_train = finally_dataframe[:2]
    MLP.fit(x_train, y_train)
    return MLP


# data visualization
def visualization(network):
    model = network
    x_test, y_test = finally_dataframe[2:]
    test_prediction = model.predict([x_test[2]])
    real_rates = y_test[2]
    plt.plot(real_rates, label='real')
    plt.plot(test_prediction[0], label='prediction')
    plt.savefig('flask_app/static/plot.png')

