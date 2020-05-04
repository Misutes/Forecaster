from datetime import datetime


# time counter decorator
def timeit(function):
    def wrapper(*args):
        start = datetime.now()
        result = function(*args)
        end = datetime.now()
        print(f'Function has worked: {end - start}')
        return result

    return wrapper
