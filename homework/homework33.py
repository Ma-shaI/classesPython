import random


class Breeding:
    SEX = ['M', 'F']
    list_dogs = []

    def __init__(self, animal, name, age, sex):
        if sex == 'M' or sex == 'F':
            self.animal = animal
            self.name = name
            self.age = age
            self.sex = sex
        else:
            raise TypeError('Введите пол собачки верно, M-мальчик, F-девочка')

    def __add__(self, other):

        if not isinstance(other, Breeding):
            raise ArithmeticError('Животные должны принадлежать к классу Breeding')
        if self.animal != other.animal:
            raise TypeError('Ой-Ой, мы не имеем права скрещивать животных разных видов')
        if self.sex == other.sex:
            raise TypeError('Животные одного пола не могут дать потомства')
        for i in range(random.randrange(1, 7)):
            self.list_dogs.append(f"{self.animal}(name='No name', age=0, sex='{random.choice(self.SEX)}')")
        return other.list_dogs

    def print_info(self):
        if self.sex == 'M':
            print(f'{self.name} is good boy!!!')
        elif self.sex == 'F':
            print(f'{self.name} is good girl!!!')

    def print_progeny(self):
        print(self.list_dogs)


Tom = Breeding('Dog', 'Tom', 2, 'M')
Tom.print_info()
Elsa = Breeding('Dog', 'Elsa', 2, 'F')
Elsa.print_info()
Tom += Elsa
Elsa.print_progeny()
