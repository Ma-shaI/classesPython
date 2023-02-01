# Упаковка данных
#
# Кодирование (сериализация)
# Декодирование (десериализация)
#
# 1. marshal (.pyc) - для кодирования данных .pyc - самый старый метод
# 2. pickle
# 3. json

# dump () - сериализует в отдельный файл (сохраняет данных в файл)
# load () - десериализует из открытого файла (считывает данных из открытого файла)

# dumps() - сериализует строку (сохраняет данные в строку ( в памяти))
# loads() - десериализует строку (считывает данные из строки (из памяти))

# import pickle

# filename = 'basket.txt'
# shop_list = {
#     'фрукты': ["яблоки", "манго"],
#     'овощи': ["морковь"],
#     'бюджет покупки': 1000,
# }
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, 'rb') as fs:
#     shop = pickle.load(fs)
#
# print(shop)


# class Test:
#     num = 35
#     st = 'Hello'
#     lst = [1,2,3]
#     d = {
#         'first': 'a', 'second': 2
#     }
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f'Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl}'
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку: \n{my_obj}\n')
#
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку: \n{l_obj}\n')


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(5)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# import json
#
# data = {
#     'name': 'Igor',
#     'hobbies': ('running', 'sky driving'),
#     'age': 20,
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 5
#         },
#         {
#             'firstName': 'Bob',
#             'age': 8
#         }]
# }
#
# # with open('data_file.json', 'w') as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open('data_file.json', 'r') as fw:
# #     data = json.load(fw)
# #     print(data)
#
# json_string = json.dumps(data, ensure_ascii=False)
# data = json.loads(json_string)
# print(data)


# Создать класс. Свойства класса сохранить в json объект

import json


# data = {
#     'name': 'Igor',
#     'hobbies': ['running', 'sky diving'],
#     'age': 20,
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 5
#         },
# {
#             'firstName': 'Bob',
#             'age': 8
#         }
#     ]
# }
#
# with open("data_file.json", "w") as fw:
#     json.dump(data, fw)

# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=4)
#
#
# for i in range(5):
#     write_json(get_person())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # n = ''
        # for i in self.marks:
        #     n += f'{i}, '
        return f'Студент: {self.name}: {", ".join(map(str, self.marks))}'

    def __repr__(self):
        return f'{self.name}: {", ".join(map(str, self.marks))}'

    def add_marks(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    # def write_json(self):
    #     try:
    #         data = json.load(open('students.json'))
    #     except FileNotFoundError:
    #         data = []
    #     data.append(f'{self.name}:{self.marks}')
    #
    #     with open('students.json', 'w') as f:
    #         json.dump(data, f, indent=4)
    #
    # def read_json(self):
    #     with open('students.json', 'r') as f:
    #         data = json.load(f)
    #         print(data)
    @staticmethod
    def dupm_to_json(stud, filename):

        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []
        data.append({'name': stud.name, 'marks': stud.marks})
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_to_file(filename):
        with open(filename, 'r') as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = "\n".join(map(str, self.students))
        return f'{self.group}:\n{a}'

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    def write_json(self):
        data_student = {}
        for i in self.students:
            m = str(i).split(': ')
            data_student[m[1]] = m[2]

        try:
            data = json.load(open('groups.json', encoding='utf-8'))
        except FileNotFoundError:
            data = {}

        data[self.group] = data_student
        with open('groups.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def read_json(self):
        with open('groups.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data)


    @staticmethod
    def dump_group(file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            stud_list = []
            for i in group.students:
                stud_list.append([i.name, i.marks])
            data.append(stud_list)
            json.dump(data, f, indent=2)

    @staticmethod
    def upload_journal(file):
        with open(file, 'r') as f:
            print(json.load(f))


s1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
s2 = Student('Nikolaenlo', [2, 3, 5, 4, 2])
s3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
sts = [s1, s2]
my_group = Group(sts, 'Группа ГК Python')
group22 = [s2]
my_group2 = Group(group22, "ГК Web")
# print(s1)
# s1.add_marks(4)
# # print(s1)
# # s1.delete_mark(3)
# # print(s1)
# # s1.edit_mark(2, 4)
# # print(s1)
# # print(s1.average_mark())
# # print(my_group)
# # print()
# my_group.add_student(s3)
# # print(my_group)
# # print()
# my_group.remove_student(1)
# # print(my_group)

# # print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print()
# print(my_group2)
# s1.write_json()
# s1.read_json()

# my_group.read_json()
#
# my_group.write_json()
# my_group2.write_json()
# my_group.read_json()
# Student.dupm_to_json(s1, 'student.json')
#
# Student.dupm_to_json(s2, 'student.json')
# Student.load_to_file('student.json')

# Group.dump_group('group.json', my_group)
# Group.upload_journal('group.json')
Group.dump_group('group.json', my_group2)
Group.upload_journal('group.json')