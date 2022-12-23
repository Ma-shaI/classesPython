import math


class Desk:
    def __init__(self, width=None, height=None, radius=None):
        self._width = width
        self._height = height
        self._radius = radius

    def square_result(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод square_result()')


class RectDesk(Desk):
    def square_result(self):
        if self._height is None:
            print(self._width ** 2)
        elif self._width is None:
            print(self._height ** 2)
        else:
            print(self._width * self._height)


class CircleDesk(Desk):
    def square_result(self):
        if self._radius:
            print(math.pi * self._radius ** 2)


s = RectDesk(10)
print(s.__dict__)
s.square_result()
s_d = RectDesk(10, 20)
print(s_d.__dict__)
s.square_result()
c_d = CircleDesk(radius=20)
print(c_d.__dict__)
c_d.square_result()
