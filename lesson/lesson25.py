# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print('я - метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('связующий метод')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('я - метод вложенного класса', MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('Внешний')
# inner = MyOuter.MyInner('Внутренний', out)
# print(out.name)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light green'
#             self.code = '024avc'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Code:', self.code)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

#
# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head =self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print('ID:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('ID:', self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# print()
# d2 =outer.head
# d2.display()

# class Computer:
#     def __init__(self, name, title, brand):
#         self.name = name
#         self.os = self.OS(title)
#         self.cpu = self.CPU(brand)
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def __init__(self, brand):
#             self.brand = brand
#
#
#         def make(self):
#             return self.brand
#
#         def model(self, model):
#             return model
#
#
# comp = Computer('PC001', 'Windows-7', 'Intel')
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make(), my_cpu.model('Core-i7'))


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

