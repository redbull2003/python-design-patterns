"""
    Structural:
      - Adapter
            Adapter => 1.Adaptee  2.Adapter  3.Client
"""
# Adapter design-pattern allow us with create interfaces that connect classes that can not work together.

class IranSocket:
    _type = '2'


class Adapter:
    _socket = None
    _pinType = '3To2'

    def __init__(self, socket):
        self._socket = socket


class Fridge:
    _adapter = None
    _pinType = '3'

    def __init__(self, adapter):
        self._adapter = adapter

    def freeze(self):
        if self._adapter._pinType == (self._pinType + 'To' + (self._adapter._socket._type)):
            print('Done...')
        else:
            print('Sorry, not usable...')

ir = IranSocket()
adapter = Adapter(ir)
f = Fridge(adapter)
f.freeze()