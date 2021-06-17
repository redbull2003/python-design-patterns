"""
    1. functions are objects.
    2. functions can be stored in data structure
    3. functions can be passed to other functions (higher-order functions)
    4. functions can be nested (inner and outer functions)
    5. functions can capture local state (lexical closure)
    6. objects can behave like functions  =>  __call__
"""


def show(name, age):
    def adult():  # lexical closure
        return f'{name} is adult'
    
    def kid():  # lexical closure
        return f'{name} is kid'

    
    if age > 18:
        return adult
    else:
        return kid

print(show('Max', 19)())

# -------------------------------------


def show(name):
    def getName(n):
        return f'Hello {n}'
    return getName(name)

print(show('Shayan'))