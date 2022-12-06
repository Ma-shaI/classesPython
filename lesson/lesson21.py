# ООП

# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# p1 = Point()
# p2 = Point()
# print('p1:', p1.x)
# print('p2:', p2.x)
# print('Point =', Point.x)
# # print(type(p1))
# p1.x = 100
# p2.x = 200
# print('p1 = ', p1.x)
# print('p2 = ', p2.x)
# print('Point=', Point.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y = 300
# Point.x = 400
# print('p1 = ', p1.y)
# print('p2 = ', p2.y)
# print('Point=', Point.y)
# print('p1 = ', p1.x)
# print('p2 = ', p2.x)
# print('Point=', Point.x)


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1


# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)  # используется для просмотра всех свойств класса или его экземпляра
# # print(Point.__dict__)


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)


# p1 =Point()
# print(p1.x)
# p1.x =5
# p1.y =10
# p1.set_coords()
# Point.set_coords(p1)
# p2 = Point()
# p2.x =2
# p2.y =7
# p2.set_coords()


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# print(p1.x)
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2, 5, 8)
# print(p2.__dict__)
# print(p2.x)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя:{self.name}\nДата рождения:{self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.country = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name('Алевтина')
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday('18.05.1995')
# print(h1.get_birthday())
