# Task 1

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = {**a, **b, **c}
# print(d)

# Task 2

# d = {'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
# По заданию
# print(d['emp3'])
# n = d['emp3']['salary']
# d['emp3'].update({'salary': 8500})
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ':', d[i][j])

# n = input('Введите номер сотрудника от 1 до 3: ')
# emp = 'emp'+n
# print(emp)
# print(d[emp])
# print('Текущая зарплата', d[emp]['name'])
# salary = int(input('Внесите изменения в зарплату: '))
# d[emp].update({'salary': salary})
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ':', d[i][j])


# Task 3

# n = int(input('Введите количество студентов: '))
# d = {input(f'{i + 1}-ый студент: '): int(input('Балл: ')) for i in range(n)}
# point = round(sum(d.values()) / n)
# print('Средний балл: ', point, '. Студенты с баллом выше среднего: ', sep='')
# for k, v in d.items():
#     if v > point:
#         print(k)
