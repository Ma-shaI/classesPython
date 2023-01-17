# import random
#
#
# class Breeding:
#     SEX = ['M', 'F']
#     list_dogs = []
#
#     def __init__(self, animal, name, age, sex):
#         if sex == 'M' or sex == 'F':
#             self.animal = animal
#             self.name = name
#             self.age = age
#             self.sex = sex
#         else:
#             raise TypeError('Введите пол собачки верно, M-мальчик, F-девочка')
#
#     def __add__(self, other):
#
#         if not isinstance(other, Breeding):
#             raise ArithmeticError('Животные должны принадлежать к классу Breeding')
#         if self.animal != other.animal:
#             raise TypeError('Ой-Ой, мы не имеем права скрещивать животных разных видов')
#         if self.sex == other.sex:
#             raise TypeError('Животные одного пола не могут дать потомства')
#         for i in range(random.randrange(1, 7)):
#             self.list_dogs.append(f"{self.animal}(name='No name', age=0, sex='{random.choice(self.SEX)}')")
#         return other.list_dogs
#
#     def print_info(self):
#         if self.sex == 'M':
#             print(f'{self.name} is good boy!!!')
#         elif self.sex == 'F':
#             print(f'{self.name} is good girl!!!')
#
#     def print_progeny(self):
#         print(self.list_dogs)
#
#
# Tom = Breeding('Dog', 'Tom', 2, 'M')
# Tom.print_info()
# Elsa = Breeding('Dog', 'Elsa', 2, 'F')
# Elsa.print_info()
# Tom += Elsa
# Elsa.print_progeny()
import random


class Cat:
    def __init__(self, name, pol, age=0):
        self.name = name
        self.pol = pol
        self.age = age

    def __str__(self):
        if self.pol == "M":
            return f"{self.name} is good boy!!!"
        elif self.pol == "F":
            return f"{self.name} is good girl!!!"
        else:
            return f"{self.name} is good Kitty!!!"

    def __repr__(self):
        return f"Cat(name='{self.name}, age={self.age}, sex='{self.pol})"

    def __add__(self, other):
        if self.pol != other.pol:
            return [Cat("No name", random.choice(['M', 'F'])) for _ in range(1, random.randint(2, 7))]
        else:
            return 'Types are not support!'


cat1 = Cat("Tom", "M")
print(cat1)
cat2 = Cat("Elsa", "F")
print(cat2)
print(cat1 + cat2)
cat3 = Cat("Elsa", "M")
print(cat1 + cat3)
lst = (cat1, cat2, cat3)
b, c = random.choices(lst, k=2)
print(b + c)
