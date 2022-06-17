from functools import wraps
import time


def timeit(param):

    def inner_function(func):
        @wraps(func)
        def timeit_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            if "index" in kwargs:
                if kwargs["index"] == 1:
                    print(
                        f'01: {str(kwargs["chains"])} Tomó {total_time:.4f} segundos')
            else:
                print(
                    f'0: Total Tomó {total_time:.4f} segundos')
        return timeit_wrapper
    return inner_function
