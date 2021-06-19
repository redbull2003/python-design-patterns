"""
    Behavioral
      - Iterator => 1.iterable, 2.iteration
            __iter__, __next__
"""
# Iterator design-pattern help us to create our personal sequence and
# determine how that sequence should be navigated

class Iteration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of sequence...')
        for i in range(0, self.value):
            value = self.value
            self.value -= 1
            return value


class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Iteration(self.value)


c1 = Iterable(7)
c2 = iter(c1)

print(next(c2))
print(next(c2))
print(next(c2))
print(next(c2))