"""
    Creational
      - Builder
"""
# Builder pattern is used when we go to make a product that product is maked another \
#  small components that those smaller componenets must be created so then we can use of them

from abc import ABC, abstractmethod

class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        wheel = self.__builder.get_wheel()
        car.set_wheel(wheel)

        engine = self.__builder.get_engine()
        car.set_engine(engine)
        return car
# ----------------------------------
class Car:
    def __init__(self):
        self.__wheel = None
        self.__engine = None
        self.__body = None
    
    def set_wheel(self, wheel):
        self.__wheel = wheel
    
    def set_body(self, body):
        self.__body = body

    def set_engine(self, engine):
        self.__engine = engine
    
    def detail(self):
        print(f'body: {self.__body.shape}')
        print(f'engine: {self.__engine.hp}')
        print(f'wheel: {self.__wheel.size}')
# ----------------------------------
class Builder(ABC):
    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_body(self):
        pass


class Lamborghini(Builder):
    def get_body(self):
        body = Body()
        body.shape = 'Sport'
        return body 

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class Corvette(Builder):
    def get_body(self):
        body = Body()
        body.shape = 'Sport'
        return body 

    def get_engine(self):
        engine = Engine()
        engine.hp = 400
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel
# ----------------------------------
class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None


car1 = Lamborghini()
director = Director()
director.set_builder(car1)
l1 = director.get_car()
l1.detail()