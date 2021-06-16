class A:
    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        if name == 'Max':
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


a1 = A('Max')

print(a1)