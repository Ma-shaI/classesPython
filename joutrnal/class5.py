# def print_text():
#     print(""""Don't let the noise of others' opinions\ndrown out your own inner voice."\n
#     \t\t\t\t\t\t\tSteve Jobs""")
# print_text()

# def info(a, b):
#     for i in range(a, b+1):
#         if i%2!=0:
#             print(i, end=' ')
#
#
# info(int(input('->')), int(input('->')))

# def info(l, s, sym):
#     if s == 'горизонт':
#         return l * sym
#     else:
#         return '\n'.join([sym for _ in range(l)])
#
#
# print(info(5, "вертикально", '*'))
#
#
# def get_max(*args):
#     return max(args)
#
#
# print(get_max(1, 55, 78, 5))


# def get_sum(a, b):
#     return sum([i for i in range(a, b + 1)])
#
#
# print(get_sum(1, 7))


# def get_simple(a):
#     count = 0
#     for i in range(2, a):
#         if a%i ==0:
#             count+=1
#
#     return not count
#
# print(get_simple(7))


# def get_happy(a):
#     if len(str(a)) == 6:
#         lst = [int(i) for i in str(a)]
#         if lst[0]+lst[1]+ lst[2] == lst[3] + lst[4] + lst[5]:
#             return True
#         else:
#             return False
#     else:
#         return 'Введите 6-тизначное число'
#
#
# print(get_happy(123420))

