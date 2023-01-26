# a = input('-> ')
# print(a[::-1])
import random

# a = input('-> ')
# c_d = 0
# c_a =0
# for i in a:
#     if i.isdigit():
#         c_d +=1
#     elif i.isalpha():
#         c_a += 1
#
# print(c_d, c_a)

# a, b = input('-> '), input('-> ')
# count = 0
# for i in [i for i in a]:
#     if b == i:
#         count += 1
# print(count)

# a, b = input('-> '), input('-> ')
# count = 0
# for i in a.split():
#     if b == i:
#         count += 1
# print(count)

# a, b, c = input('-> '), input('-> '), input('-> ')
# print(a.replace(b, c))

# lst = [int(input('-> ')) for i in range(5)]
# n = int(input('->'))
# count = 0
# for i in lst:
#     if i == n:
#         count += 1
# print(count)

# lst = [int(input('->')) for i in range(7)]
# print(sum(lst))
# print(sum(lst)/len(lst))

# lst = [random.randint(-10000, 10000) for i in range(random.randint(1, 15))]
# print(lst)
# sum_ot = 0
# summa_t = 0
# summa_nt = 0
# s = 1
# ind_max = 0
# ind_min =0
# for i in range(len(lst)):
#     if lst[i] < 0:
#         sum_ot += lst[i]
#     if lst[i] % 2 == 0:
#         summa_t += lst[i]
#     else:
#         summa_nt += lst[i]
#     if i%3 == 0:
#         s *= lst[i]
#     if lst[i] == max(lst):
#         ind_max = i
#     if lst[i] == min(lst):
#         ind_min = i
# print(sum_ot)
# print(summa_t)
# print(summa_nt)
# print(s)

lst = [random.randint(-1000, 10000) for i in range(random.randint(1, 15))]
print(lst)
lst1 = [i for i in lst if i % 2 == 0]
print(lst1)
lst2 = [i for i in lst if i % 2 != 0]
print(lst2)
lst3 = [i for i in lst if i < 0]
print(lst3)
lst4 = [i for i in lst if i > 0]
print(lst4)
