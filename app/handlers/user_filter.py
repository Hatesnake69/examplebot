from aiogram import types, Dispatcher


def registration_check(func):
    def wrapped_func(*args, **kwargs):
        for arg in args:
            print(arg)
        for kwarg in kwargs:
            print(kwarg)
        return func(*args, **kwargs)

