from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def show(self):
        pass


class B(A):
    def show(self):
        print('show method')


b1 = B()
b1.show()