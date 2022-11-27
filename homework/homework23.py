# Task 1
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# def count(lst):
#     arr = lst[:]
#     ind = 0
#     while True:
#         try:
#             while isinstance(arr[ind], list):
#                 item = arr.pop(ind)
#                 for i in reversed(item):
#                     arr.insert(ind, i)
#             ind += 1
#         except IndexError:
#             break
#     return ind
#
#
# print(count(names))


# Task 2

numbers = [-2, 3, 8, -11, -4, 6]


def count(num):
    if not num:
        return 0
    else:
        cnt = count(num[1:])
        if num[0] < 0:
            cnt += 1
        return cnt


print(count(numbers))