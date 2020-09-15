# retry_decorator.py
import functools
import time


def retry(interval, max_retries=3, exceptions=None):
    if exceptions is None:
        exceptions = Exception

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    res = func(*args, **kwargs)
                    return res
                except exceptions:
                    time.sleep(interval)
                    pass
            res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator


def retry(max_retries=3, exceptions=None, interval=0):
    if exceptions is None:
        exceptions = Exception

    def decorator(func):
        # @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(interval)
            return func(*args, **kwargs)

        return wrapper

    return decorator


i = 0


@retry(interval=0.5)
def my_func():
    global i
    i += 1
    print(i)
    raise Exception


def main():
    print(my_func.__name__)
    my_func()


if __name__ == '__main__':
    main()
