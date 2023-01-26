# tpl= ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana', 'banana', 'apple', 'mango')
# fr = input('->')
# def print_count(tpl, fruit):
#     count = 0
#     for i in tpl:
#         if i == fruit:
#             count +=1
#
#     return count
#
#
# print(print_count(tpl, fr))


# tpl= ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana', 'banana', 'apple', 'mango')
# fr = input('-> ')
#
# def print_count(tp, fruit):
#     count = 0
#     for i in tp:
#         if fruit in i:
#             count +=1
#
#     return count
#
#
# print(print_count(tpl, fr))

# tpl = ('Audi', 'BMW', 'Porsche', 'Lada', 'Infiniti', 'Reno', 'BMW', 'Audi', 'AUDI')
# n = input('-> ')
# w = input('-> ')
#
# m = list(tpl)
# for i in range(len(m)):
#     if m[i] == n:
#
#         m[i] = w
# tpl = m
# print(m)

#
# tpl = [1, 1, 1, 3, 1, 5, 6, 7, 7, 8, 5, 7, 3, 6, 9, 0]
# dct = {}
# for i in tpl:
#     if i not in dct:
#         dct[i] = 1
#     else:
#         dct[i] += 1
# print(dct)

# a = {'Russia', 'USA', 'Germany', 'France', 'Italy', 'China'}
# n = input('->')
# a.add(n)
# print(a)
# el = input('->')
# a.remove(el)
# print(el)
# elem = input('->')
# for i in a:
#     if elem in i:
#         print(i)
# element = input('-> ')
# print(a.isdisjoint(element))

a = {'Kirov', 'Moscow', 'New York', 'Boston', 'Paris', 'Rim'}
b = {'Moscow', 'Rim', 'Paris', 'Tokio', 'Istanbul', 'Munich'}
# m = a & b
# print(m)
# m = a - b
# print(m)
# m = b - a
# print(m)
m = a^b
print(m)