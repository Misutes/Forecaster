from datetime import datetime
from flask_app.app import application
import flask_app.view
from Predictor import building_model, visualization


# time counter decorator
def timeit(function):
    def wrapper(*args):
        start = datetime.now()
        result = function(*args)
        end = datetime.now()
        print(f'Function has worked: {end - start}')
        return result

    return wrapper


if __name__ == '__main__':
    application.run()