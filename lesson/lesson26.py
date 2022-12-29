# Множественное наследование - несколько родителей, дочерний берет все методы от родителей.
# По возможности лучше не использовать

# class Creature:
#     def __init__(self, name):
#         self.name = name
# 
# 
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
# 
# 
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
# 
# 
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
# 
# 
# beast = Dog('Buddy')
# beast.bark()
# beast.play()
# beast.sleep()

# class A:
#     def __init__(self):
#         print('A')
#
#
# class B(A):
#     # def __init__(self):
#     #     print('B')
#
#     def hi(self):
#         print('B_hi')
#
#
# class C(A):
#     # def __init__(self):
#     #     print('C')
#
#     def hi(self):
#         print('C_hi')
#
#
# class D(B, C):
#     # def __init__(self):
#     #     C.__init__(self)
#     #     B.__init__(self)
#     #     print('D')
#     def hi(self):
#         C.hi(self)
#         B.hi(self)
#         print('D_hi')
# d = D()
# d.hi()
# print(D.mro())

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         Style.__init__(self, *args)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color='red', width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()


# Миксин (примеси) - вид множественного наследования, чтобы не дублировать код
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# sub = MySubClass()
# sub.display('Строка будет отображаться и регистрироваться в файле')


