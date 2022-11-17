from math import pi


# Task 1
# def func(*args):
#     pr = 1
#     for i in args:
#         pr *= i
#     return pr
#
#
# print(func(10,9))
# print(func(2,3,4))
# print(func(3,5,10,6))

# Task 2
def sum_elem(*args):
    lst = [0]
    for i in args:
        lst.append(i + lst[-1])
    return lst


print(*sum_elem(3, 9, 1)[1:])
print(*sum_elem(2, 5, 4, 2)[1:])
print(*sum_elem(3, 5, 10, 6, 3)[1:])

# Task 3

# def figure(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         return (kwargs['d1'] * kwargs['d2']) / 2
#     elif figure_type == 'square':
#         return kwargs['a'] ** 2
#     elif figure_type == 'trapezoid':
#         return 1 / 2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
#     elif figure_type == 'circle':
#         return pi * kwargs['r'] ** 2
#     else:
#         return 'invalid data'
#
#
# print(figure(figure_type='rhombus', d1=10, d2=8))
# print(figure(figure_type='square', a=5))
# print(figure(figure_type='trapezoid', a=12, b=3, h=6))
# print(figure(figure_type='circle', r=18))
# print(figure(figure_type='unknown', a=1, b=2, c=3))

