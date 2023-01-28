class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        if not isinstance(value, int) or value < 0:
            raise ValueError(f'Сторона треугольника {value} должна быть положительным целым числом')

        else:
            instance.__dict__[self.name] = value


class Triangle:
    a = NonNegative()
    b = NonNegative()
    c = NonNegative()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.c):
            return (f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует')
        else:
            return (f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует')


t1 = Triangle(2, 5, 6)
print(t1.info())
t2 = Triangle(5, 2, 8)
print(t2.info())
t3 = Triangle(7, 3, 6)
print(t3.info())
