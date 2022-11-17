# множества (set)

# s = {'banana', 'apple', 'orange', 'apple', 'banana'}
# print(type(s))
# print(s)
# print(len(s))

# c = ['hello', 'world']
# a = set(c)
# print(a)

# s = {x*x for x in range(10)}
# print(s)

# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = set(num)
# print(num)
# num = list(num)
# print(num)

# def to_set(element):
#     return set(element), len(set(element))
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {'red', 'green', 'blue'}
# print('green' in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r }
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# a.remove('Tom')
# print(a)
# user = 'Tom'
# if user in a:
#     a.remove('Tom')
# print(a)
# a.discard('Bob')
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b) - объединение множеств
# c = a | b
# print(c)
# a |= b  # a.update(b)
# c = a & b  # a.intersection(b) - пересечение множеств
# print(c)
# a &= b  # a.intersection_update(b)
# print(a)
# c = a - b  # a.difference(b) - разность множеств
# print(c)
# c = a ^ b  # a.symmetric_difference(b) - симметричная разность
# print(c)

# s1, s2, s3, s4, s5, s6, s7 = {1, 2}, {3}, {4, 5}, {3, 2, 6}, {6}, {7, 8}, {9, 8}
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print('Unic elem count:', len(s))
# print('Min elem:', min(s))
# print('Max elem:', max(s))

# a = 'Hello'
# b = 'How are you'
# s = set(a) & set(b)
# print('Общими буквами являются:', s)

# s1 = set(input('Введите первую строку: '))
# s2 = set(input('Введите вторую строку: '))
# s = s1 - s2
# print('Искомыми буквами являются:', s)


# s1 = {'Marina', 'Jenya', 'Sveta'}
# s2 = {'Kostya', 'Jenya', 'Ilya'}
# s = s1 ^ s2
# print('Only one hobby:', s)
# both_hobby = s1 & s2
# print('Both hobbies:', both_hobby)
# drawing = s1 - both_hobby
# print('Drawing:', drawing)

# s = frozenset([1, 2, 3, 4, 5, 4])
# print(s)
#
# a = frozenset({'hello', 'world'})
# print(a)
