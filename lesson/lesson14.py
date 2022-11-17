# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('code after')
#
#     return wrap
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print('code after')
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции: ', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# @cnt
# def bye():
#     print('Good bye')
#
#
# hello()
# # hello()
# # hello()
# bye()
# bye()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('*' * 50)
#         fn(arg1, arg2)
#         print('*' * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут,', first, last)
#
#
# print_full_name('Ирина', "Лаврова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print('*' * 50)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         print('*' * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study)
#
# @args_decorator
# def hello():
#     print('hello')
#
#
# print_full_name('Ирина', 'Борис', 'Светлана', study='JavaScript')
# print()
# print_full_name('Владимир', 'Екатерина', 'Виктор')
# hello()

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x,args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(n):
#     def return_mult(fn):
#         def wrap(num):
#             return 'Результат:', fn(num) *n
#
#         return wrap
#
#     return return_mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(7))
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Некорректный тип данных')
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError('Некорректный тип данных')
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z='Hello'):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Doge'))
# print(typed_fn2('Hello, ', 'World', '!'))
# print(typed_fn3('Hello, ', 'World', z=5))




# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end='')
#             fn(*args)
#         return wrap
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# hello_world2('Hi!')
# hello_world('world!')
