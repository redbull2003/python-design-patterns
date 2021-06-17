# Data-Structure => list, tuple, dict, set, ...
# object <=> class

class A:
    def __init__(self, *args, **kwargs):
        print('Hello World')

    def __call__(self, *args, **kwargs):
        pass


a1 = A()  # () means called

a1()