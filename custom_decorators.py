"""
    Python Decorators
"""
import functools

def outer_deco(n1):
    def outer_upper(func):
        @functools.wraps(func)
        def inner_upper(t, *args, **kwargs):
            'inner upper function'
            f = func(t)
            text = f.upper()
            print(n1)
            return text
        return inner_upper
    return outer_upper


def outer_split(func):
    def inner_split(t, *args, **kwargs):
        f = func(t)
        text = f.split(' ')
        return text
    return inner_split


@outer_split # 2nd executed
@outer_deco('shayan') # 1st executed
def show(text):
    'show function'
    return text

# print(show('Hello World', 'X'))
print(show.__name__)