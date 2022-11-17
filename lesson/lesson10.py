# en = ["red", "green", "blue"]
# j = 1
# for i in en:
#     print(j,'-й цвет: ', i, sep="")
#     j += 1

# en = ["red", "green", "blue"]
# for j, i in enumerate(en, 1):
#     print(j, '-й цвет: ', i, sep="")

# en = {0: 1, 1: 2, 2: 3}
# for i, j in enumerate(en):
#     print(i, ': ', j, '->', en[j], sep='')

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7,8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))


# def to_sa(*args):
#     n = sum(args) / len(args)
#     lst = []
#     for i in args:
#         if i < n:
#             lst.append(i)
#     return n, lst
#
#
# print(*to_sa(1, 2, 3, 4, 5, 6, 7, 8, 9), sep='\n', end='\n')
# print(*to_sa(3, 6, 1, 9, 5), sep='\n', end='\n')


# def func(a, *args):
#     return a, args
#
#
# print(func(1, 2,3,'abc'))

# def print_scores(stud, *scores):
#     print('Student name:', stud)
#
#     for score in scores:
#         print(score, end=' ')
#     print()
#
#
# print_scores('Jnonatan', 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33)


# def func(*args, ):
#     lst = []
#     for i in args:
#         lst.append(int(str(i)[::-1]))
#     return lst
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))

# def revers_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     lst = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             lst.append(revers_num(i))
#     return lst
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))

# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print('*'*20)
#
#
# info(first_name='Irina', last_name='Petrova', age=22, phone=1234567890)
# info(first_name='Igor', last_name='Ivanov', age=36, email='igor@gmail.com', country='Russia', phone=6789012345)


# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict ={'one': 'firs'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# def func(a, *args,one=True,  **kwargs):
#     return a, args,one, kwargs
#
#
# print(func(5, 9, 7, 8, 6, one=False, b=2, c=3, d=4))
