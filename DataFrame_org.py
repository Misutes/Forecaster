import pandas as pd
import Parser
import numpy as np


exchange_rates = Parser.get_exchange_rates()

# formation constant
past_days = 14
future_days = 7
start_learning = 14
end_learning = len(exchange_rates) - 7
days_columns = [f'day_{i}' for i in reversed(range(1, future_days + past_days + 1))]


# creation of a list of lists of course past_days and future_days
def learning_date():
    learning_date_list = [(exchange_rates[(i - past_days):(i + future_days)]) for i in
                          range(start_learning, end_learning)]
    return learning_date_list


# creation pandas.DataFrame from the data returned by the function above
def dataframe_formation(date):
    dataframe = pd.DataFrame(data=date, columns=days_columns)
    train_dataframe = dataframe[:-5]
    length_train_df = len(train_dataframe)
    test_dataframe = dataframe[-5:]
    length_test_df = len(test_dataframe)

    # preparing data for model training and testing
    def creating_date(dataframe, length):
        array_x = np.zeros((length, past_days, future_days))
        array_y = np.zeros((length, past_days))
        for line in range(length):
            for x in range(past_days):
                array_x[line, x] = np.array(dataframe.iloc[line][x:x + 7], dtype=np.float32)
                array_y[line, x] = np.array(dataframe.iloc[line][x + 7], dtype=np.float32)
        array_x = array_x.reshape((length, future_days * past_days))
        array_y = array_y.reshape((length, past_days))
        return array_x, array_y

    x_train, y_train = creating_date(train_dataframe, length_train_df)
    x_test, y_test = creating_date(test_dataframe, length_test_df)

    return x_train, y_train, x_test, y_test


# general function
def learning_dataframe():
    date = learning_date()
    return dataframe_formation(date)
