# wrapper.py
import functools
import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("wrapper of decorator")
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(x):
    print(x)


def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("wrapper of decorator")
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet1(message):
    print(message)


def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print("wrapper of decorator repeat")
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(3)
def greet2(m):
    print(m)


def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print("decorator")
                func(*args, **kwargs)

        return wrapper

    return my_decorator


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print('decorator')
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(2)
def greet4(m):
    print(m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print('decorator')
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet5(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print('in decorator')
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet6(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print('decorator')
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet7(m):
    print(m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(i + 1)
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet9(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(i)
                func(*args, *kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*agrs, **kwargs):
            for i in range(num):
                print(i)
                func(*agrs, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello1(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*agrs, **kwargs):
            for i in range(num):
                print(i)
                func(*agrs, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello3(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(i)
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello5(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(i)
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello7(m):
    print('hello', m)


def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(i)
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello9(m):
    print('hello', m)


def timeSpent(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(time.perf_counter() - start)
        return res

    return wrapper


@timeSpent
def add(x, y):
    time.sleep(0.1)
    return x + y


def timeSpent(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print("time spent", time.perf_counter() - start)
        return res

    return wrapper


@timeSpent
def add(x, y):
    time.sleep(0.5)
    return x + y


def main():
    greet(123)
    print(greet.__name__)

    greet1(123)
    print(greet1.__name__)

    greet2(234)

    greet4("hello")
    print(greet4.__name__)

    greet5('apple')
    print(greet5.__name__)

    greet6('ben')
    print(greet6.__name__)

    greet7('cindy')
    print(greet7.__name__)

    greet9('du')
    print(greet9.__name__)

    hello('ella')
    print(hello.__name__)

    hello1('Fill')
    print(hello1.__name__)

    hello3('Reese')
    print(hello3.__name__)

    hello5(5)
    print(hello5.__name__)

    hello7('alice')
    print(hello7.__name__)

    hello9('bob')
    print(hello9.__name__)
    print(add(1, 3))
    print(add.__name__)


if __name__ == '__main__':
    main()
