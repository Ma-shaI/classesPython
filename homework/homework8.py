# Task 1

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# for row in range(len(matrix)+1):
#     for x in range(len(matrix)):
#         print(matrix[x][row], end='\t')
#     print()


# Task 2

# from random import *
#
# mtrx = [[randint(0, 10) for _ in range(6)] for _ in range(6)]
# for row in mtrx:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# lst = [randint(0, 10) for _ in range(6)]
# print(lst)
# print()
#
# for row in range(len(mtrx)):
#     if row % 2:
#         for x in range(len(mtrx[row])):
#             print(mtrx[row][x], end='\t')
#         print()
#     else:
#         for x in lst:
#             print(x, end='\t')
#         print()

print(sum(range(0,15)))
