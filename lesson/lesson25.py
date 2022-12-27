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

class Color:
    def __init__(self):
        self.name = 'Green'
        self.lg = self.LightGreen()

    def show(self):
        print('Name:', self.name)

    class LightGreen:
        def __init__(self):
            self.name = 'Light green'
            self.code = '024avc'

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)


outer = Color()
outer.show()
g = outer.lg
g.display()
