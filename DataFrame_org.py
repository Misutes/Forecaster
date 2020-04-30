import pandas as pd
import Parser
import numpy as np


exchange_rates = Parser.get_exchange_rates()

# Formation constant
past_days = 14
future_days = 7
start_learning = 14
end_learning = len(exchange_rates) - 7

past_days_columns = [f'past_day_{i}' for i in reversed(range(1, past_days + 1))]
future_days_columns = [f'future_day_{i}' for i in range(1, future_days + 1)]


def learning_date():
    learning_date_list = [(exchange_rates[(i - past_days):(i + future_days)]) for i in
                          range(start_learning, end_learning)]
    return learning_date_list


def dataframe_formation(date):
    dataframe_exra = pd.DataFrame(data=date, columns=(past_days_columns + future_days_columns))
    X = dataframe_exra[past_days_columns][:-5]
    Y = dataframe_exra[future_days_columns][:-5]
    X_test = dataframe_exra[past_days_columns][-5:]
    Y_test = dataframe_exra[future_days_columns][-5:]
    return X, Y, X_test, Y_test


def learning_dataframe():
    date = learning_date()
    return dataframe_formation(date)


learning_dataframe()