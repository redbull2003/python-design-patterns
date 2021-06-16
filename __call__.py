class A:
    def __init__(self, *args, **kwargs):
        print('Hello World')

    def __call__(self, *args, **kwargs):
        print('Instance Created')


a1 = A()

a1()