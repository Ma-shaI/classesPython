# Task 1
# n = int(input('Введите начало диапазона: '))
# m = int(input('Введите конец диапазона: '))
# for i in range(n, m + 1):
#     if (i % 2 != 0):
#         print(i, end=' ')

# Task2
# import random
# n = random.randint(1, 100)
# count = 0
# while True:
#     m = int(input('Введите число от 1 до 100: '))
#     if 0 <= int(m) <= 100:
#         m = int(m)
#         if m == n:
#             print('Вы угадали число с', count + 1, 'раза')
#             break
#         elif m == 0:
#             if count == 0:
#                 print('Вы даже не начали игру. Количество попыток:', count)
#             print('Вы завершили игру. Количество ваших попыток:', count)
#             break
#         elif n > m:
#             print('Загаданное число больше')
#             count += 1
#         elif n < m:
#             print('Загаданное число меньше')
#             count += 1
#     else:
#         print('Вам нужно ввести число в диапазоне от 1 до 100!')

#
# # Task3
#
#
size = int(input('Введите размер поля: '))
amount = int(input('Введите количество символов: '))
for i in range(size):
    for n in range(amount):
        for j in range(size):
            for m in range(amount):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    print('* ', end='')
                elif (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                    print('  ',  end='')
            print(end='')
        print(end='\n')





