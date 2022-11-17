# Область видимости (scope)

# for i in range(5):
#     a = 5
#     print(i)
# print('a за пределами цикла', a)

# if True:
#     a = 5
# print('a =', a)

# name = 'Tom'
#
#
# def hi():
#     print('Hello,', name)
#
#
# def bye():
#     global name
#     name = 'Bob'
#     print('Good bye,', name)
#
#
# def func():
#     global surname
#     name = 'Nick'
#     surname = 'Ivanov'
#     print('name:', name, surname)
#
#
# hi()
# bye()
# func()
# print(name)
# print(surname)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))

# x = 3
#
#
# def func(a):
#     x = 2
#
#     def inner():
#         print('x =', x)  # 2
#         return a + x
#     return inner()
#
#
# print(func(5))  # 7


# import builtins
#
# print(dir(builtins))
