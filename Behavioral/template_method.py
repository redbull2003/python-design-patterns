"""
    Behavioral
      - templtae_method
"""
# Template_Method pattern defines the skeleton of an algorithm in the \
# superclass but allows subclasses to ignore certain steps of the algorithm\
# without changing its structure

from abc import ABC, abstractmethod


class Top(ABC):
    def template_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.forth_require()
        self.hook()

    def first_common(self):
        print('I am first common...')

    def second_common(self):
        print('I am second common...')

    @abstractmethod
    def third_require(self):
        pass

    @abstractmethod
    def forth_require(self):
        pass

    def hook(self):
        pass


class One(Top):
    def third_require(self):
        print('I am Third require from One...')

    def forth_require(self):
        print('I am Forth require from One...')

    def hook(self):
        print('I am hook from One...')


class Two(Top):
    def third_require(self):
        print('I am Third require from Two...')
    
    def forth_require(self):
        print('I am Forth require from Two...')


def client(class_):
    class_.template_method()


client(Two())