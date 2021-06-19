"""
    Creational:
      - Singleton
"""

# Singleton Pattern allow us to create classes in such a way that can created \
#  just one instance from that class
class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class Db(metaclass=Singleton):
    pass

d1 = Db()
d2 = Db()

print(id(d1))
print(id(d2))