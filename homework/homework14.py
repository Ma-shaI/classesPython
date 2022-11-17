# Task 1

# def func_compute(y):
#     def inner(x):
#         return x*y
#     return inner
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
# res = func_compute(3)
# print(res(15))
# print(res(20))

# Task 2 Variant 1

# def func(a, b, c):
#     def inner():
#         s = a * b
#         return s
#
#     return 2 * (inner() + a * c + b * c)


# Task 2 Variant 2


# def func(a, b, c):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s = a * b
#
#     inner()
#     return 2 * (s + a * c + b * c)

# Task 2 Variant 3


# def func(a, b, c):
#     def inner():
#         global s
#         s = a * b
#         return s
#
#     inner()
#     return 2 * (s + a * c + b * c)

#
# print(func(2, 4, 6))
# print(func(5, 8, 2))
# print(func(1, 6, 8))
