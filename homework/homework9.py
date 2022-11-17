def ret_tuple(a, b):
    if b not in a:
        return tuple()
    elif a.count(b) == 1:
        return a[a.index(b):]
    else:
        return a[a.index(b):a.index(b, a.index(b) + 1) + 1]


print(ret_tuple((1, 2, 3), 8))
print(ret_tuple((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(ret_tuple((1, 2, 8, 5, 1, 2, 9), 8))
tpl = tuple(int(input('-> ')) for i in range(int(input('Введите размер кортежа: '))))
num = int(input('Введите число: '))
print(ret_tuple(tpl, num))