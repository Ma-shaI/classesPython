# Рекурсия

# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком вы этаже: '))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) ==1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n//base, base) +convert[n%base]
#
# print(to_str(769, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


# print(type(names[0]))
# print(isinstance(names[0], list))
# print(isinstance(names[1][1][0], list))

# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#         else:
#             cnt += 1
#     return cnt
#
#
# print(count(names))

# def union(s):
#     if not s: # s == []:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))
#     return s[:1] + union(s[1:])
#
# print('Выпрямленный список:', union(names))

#
# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0]==' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
# print(remove("  Hello\tWorld   "))

