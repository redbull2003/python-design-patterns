"""
    Behavioral
      - Chain Of Responsibility
"""
# when our program is going to receive a diferrent information /
#  and return a diferrent response to that type, we can use Chain Of Responsibility pattern

from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self.proccessRequest(request)
        if not handled:
            self._successor.handle(request)

    @abstractmethod
    def proccessRequest(self, request):
        pass


class HandlerOne(AbstractHandler):
    def proccessRequest(self, request):
        if 0 < request <= 10:
            print(f'Handler one is proccessing this request... {request}')
            return True


class HandlerTwo(AbstractHandler):
    def proccessRequest(self, request):
        if 10 < request <= 20:
            print(f'Handler two is proccessing this request... {request}')
            return True


class DefaultHandler(AbstractHandler):
    def proccessRequest(self, request):
        print(f'This request has no handler, so default handler is proccessing this request... {request}')
        return True


class Client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


request = [7, 17, 77, 13]

c1 = Client()
c1.delegate(request)