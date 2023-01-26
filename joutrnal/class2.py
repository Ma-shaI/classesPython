# a = int(input('-> '))
# print('Even number' if a % 2 == 0 else 'Odd number')

# a = int(input('-> '))
# print('Number is multiple 7' if not a % 7 else 'Number is not multiple 7')

# a, b = int(input('->')), int(input('->'))
# print(a if a > b else b)
#
# a, b = int(input('-> ')), int(input('-> '))
# print(a if a < b else b)


# a = int(input('->'))
# if len(str(a)) == 6:
#     m = [int(i) for i in str(a)]
#     if m[0]+m[1]+m[2] == m[3]+m[4]+m[5]:
#         print(a, 'is happy')
#     else:
#         print(a, 'is not happy')
# else:
#     print('Введите 6тизначное число')

# a = int(input('-> '))
# if len(str(a)) == 6:
#     m = [int(i) for i in str(a)]
#     m[0], m[5] = m[5], m[0]
#     m[1], m[4] = m[4], m[1]
#     s = ''
#     for i in m:
#         s += str(i)
#     print(int(s))
# else:
#     print('Введите 6тизначное число')

# a = int(input('-> '))
#
# if a == 1 or a == 2 or a == 12:
#     print('Winter')
# elif 3 <= a <= 5:
#     print('Spring')
# elif 6 <= a <= 8:
#     print('Summer')
# elif 9 <= a <= 11:
#     print('Autumn')
# else:
#     print('Error')
