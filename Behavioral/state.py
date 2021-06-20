"""
    Behavioral
      - State
"""
# State design-pattern allow an object to change the behavioral when internal \
# state changes

class State:
    def operate(self):
        print(f'Turning TV {self.status}')


class TurnOn(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'On'
    
    def change_state(self):
        print('Changing state to Off...')
        self.tv.state = self.tv.off


class TurnOff(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'Off'

    def change_state(self):
        print('Changing state to On...')
        self.tv.state = self.tv.on


class TV:
    def __init__(self):
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.off

    def press(self):
        self.state.operate()
        self.state.change_state()


t = TV()
t.press()