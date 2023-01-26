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

data = {
    'name': 'Igor',
    'hobbies': ['running', 'sky diving'],
    'age': 20,
    'children': [
        {
            'firstName': 'Alice',
            'age': 5
        },
{
            'firstName': 'Bob',
            'age': 8
        }
    ]
}

with open("data_file.json", "w") as fw:
    json.dump(data, fw)