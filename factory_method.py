"""
    Creational:
      - Factory Method:
            3 Component => 1.Creator, 2.Product, 3.Client
"""

# Factory Method allows us to create a super_class that is responsible \
#  for creating an object and allow the sub_class to be able to change the type of object being made

from abc import ABC, abstractmethod

# -------------------------------- Creator
class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit()
        return result

class JsonCreator(Creator):
    def make(self):
        return Json() # Return Products
    

class XmlCreator(Creator):
    def make(self):
        return Xml() # Return Products
# ---------------------------------

# --------------------------------- Product
class Product(ABC):
    @abstractmethod
    def edit(self):
        pass


class Json(Product):
    def edit(self):
        return 'Editing Json file'


class Xml(Product):
    def edit(self):
        return 'Editing Xml file'
# --------------------------------

# -------------------------------- Client
def client(format):
    return format.call_edit()
# --------------------------------    

print(client(JsonCreator()))





# ================================================== simple sample ==================================================

class A:
    def __init__(self, name, format):
        self.name = name
        self.format = format


class B:
    def edit(self, file): # Client
        edit = self._get_edit(file)
        return edit(file)

    def _get_edit(self, file): # Creator
        if file.format == 'json': # Identifier
            return self.json_edit
        elif file.format == 'xml': # Identifier
            return self.xml_edit
        else:
            raise ValueError('This type of file is not supported')
    
    def json_edit(self, file): # Product
        print(f'Editing Json file... {file.name}')

    def xml_edit(self, file): # Product
        print(f'Editing Xml file... {file.name}')


a1 = A('first', 'xml')
b1 = B()
b1.edit(a1)