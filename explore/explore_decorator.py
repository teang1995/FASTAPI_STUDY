import datetime

def trace(func):
    def wrapper():
        print(func.__name__, "함수 시작")
        func()
        print(func.__name__, "함수 끝")

    return wrapper


class DatetimeDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())


@trace
def hello():
    print("hello")


@DatetimeDecorator
def world():
    print("world")


if __name__ == "__main__":
    hello()
    world()