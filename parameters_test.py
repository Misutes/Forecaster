from sklearn.metrics import mean_squared_error as mse
from Predictor import building_model
from DataFrame_org import learning_dataframe
from datetime import datetime

finally_dataframe = learning_dataframe()


def timeit(function):
    def wrapper(*args):
        start = datetime.now()
        result = function(*args)
        end = datetime.now()
        print(f'Function has worked: {end - start}')
        return result
    return wrapper


@timeit
def test_parameters(dataframe, network):
    print('Start testing')
    X_test, Y_test = dataframe[2:]
    real_rates = Y_test.iloc[0]
    global_error_dict = {}
    local_error_dict = {}
    limit_par_one = [50, 300, 1]
    limit_par_two = [10, 250, 1]
    for (i, par_one) in zip(range(1, limit_par_one[1]), range(*limit_par_one)):
        global_error_dict.setdefault(f'par_one_{i}')
        global_error_dict[f'par_one_{i}'] = {}
        for (j, par_two) in zip(range(1, limit_par_two[1]), range(*limit_par_two)):
            model = network(par_one, par_two)
            prediction = model.predict([X_test.iloc[0]])
            global_error_dict[f'par_one_{i}'].setdefault(f'par_two_{j}', mse(real_rates, prediction[0]))
        local_error_dict.setdefault(f'par_one_{i}')
        min_error = min(global_error_dict[f'par_one_{i}'].items(), key=lambda x: x[1])
        local_error_dict[f'par_one_{i}'] = min_error
    main_error = min(local_error_dict.items(), key=lambda x: x[1][1])
    max_iter = main_error[0].split('_')[2]
    hidden_layer_sizes = main_error[1][0].split('_')[2]
    print(f'max_iter: {max_iter}', f'hidden_layer_sizes: {hidden_layer_sizes}')


test_parameters(finally_dataframe, building_model)