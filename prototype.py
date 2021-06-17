"""
    Creational:
      - Protoype
"""
# Prototype pattern helps us to make a copy of an object that was created already /
#  so that there is no need to create an new object and save the resources.
import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:
    def __init__(self):
        self._objects = {}
    
    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


p1 = Person('Shayan', 18)

pro1 = Prototype()
pro1.register('person1', p1)
PersonCopy = pro1.clone('person1')

print(PersonCopy.__dict__)