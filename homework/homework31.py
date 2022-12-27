import math


#
#
# class Desk:
#     def __init__(self, width=None, height=None, radius=None):
#         self._width = width
#         self._height = height
#         self._radius = radius
#
#     def square_result(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод square_result()')
#
#
# class RectDesk(Desk):
#     def square_result(self):
#         if self._height is None:
#             print(self._width ** 2)
#         elif self._width is None:
#             print(self._height ** 2)
#         else:
#             print(self._width * self._height)
#
#
# class CircleDesk(Desk):
#     def square_result(self):
#         if self._radius:
#             print(math.pi * self._radius ** 2)
#
#
# s = RectDesk(10)
# print(s.__dict__)
# s.square_result()
# s_d = RectDesk(10, 20)
# print(s_d.__dict__)
# s.square_result()
# c_d = CircleDesk(radius=20)
# print(c_d.__dict__)
# c_d.square_result()


# Правильный вариант

class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            if length is None:
                self._width = self._length = width
            else:
                self._width = width
                self._length = length
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод calc_area()')


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(math.pi * self._radius ** 2, 2)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())

t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())
