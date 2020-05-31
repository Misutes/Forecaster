from sklearn.metrics import mean_squared_error as mse
from Predictor import building_model
from DataFrame_org import learning_dataframe
from Global import timeit
import itertools


finally_dataframe = learning_dataframe()


# selection of parameters with the minimum standard deviation the test sample
@timeit
def test_parameters(dataframe, network):
    print('Start testing')
    x_test, y_test = dataframe[2:]
    real_rates = y_test[0]
    global_error_dict = {}
    local_error_dict = {}
    limit_par_one = [50, 250]
    step_par_one = 1
    limit_par_two = [50, 250]
    step_par_two = 1

    # selection quantity of hidden_layers
    def layers_test():
        list_layers = []
        max_layers = 2
        for layer in range(*limit_par_two, step_par_two):
            print(layer)
            right_list, revers_list = list(range(1, layer)), list(reversed(range(1, layer)))
            for length in range(1, max_layers + 1):
                right_layers = (
                    [list(x) for x in itertools.combinations_with_replacement(right_list, length) if sum(x) == layer])
                reverse_layers = sorted(
                    [list(x) for x in itertools.combinations_with_replacement(revers_list, length) if sum(x) == layer])
                local_layers = right_layers + reverse_layers
                if not len(local_layers):
                    list_layers.append([layer])
                if len(local_layers):
                    for y in local_layers:
                        permutation = list(itertools.permutations(y, length))
                        for z in range(len(permutation)):
                            obj = list(permutation[z])
                            if obj not in list_layers:
                                list_layers.append(obj)
        return list_layers

    global_layers = layers_test()
    print(global_layers)
    for par_one in range(*limit_par_one, step_par_one):
        global_error_dict.setdefault(f'par_one_{par_one}')
        global_error_dict[f'par_one_{par_one}'] = {}
        for element in global_layers:
            model = network(par_one, element)
            prediction = model.predict([x_test[0]])
            global_error_dict[f'par_one_{par_one}'].setdefault(f'par_two_{element}', mse(real_rates, prediction[0]))
        local_error_dict.setdefault(f'par_one_{par_one}')
        min_error = min(global_error_dict[f'par_one_{par_one}'].items(), key=lambda x: x[1])
        if float(min_error[1]) >= .01:
            local_error_dict[f'par_one_{par_one}'] = min_error
    main_error = min(local_error_dict.items(), key=lambda x: x[1][1])
    print('mean square deviation:', main_error[1][1])
    max_iter = main_error[0].split('_')[2]
    hidden_layer_sizes = main_error[1][0].split('_')[2]
    print(f'max_iter: {max_iter}', f'hidden_layer_sizes: {hidden_layer_sizes}')


test_parameters(finally_dataframe, building_model)
