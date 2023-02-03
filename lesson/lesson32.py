# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
# top_users = (sorted(todos_by_user.items(), key=lambda item: item[1], reverse=True))
# print(top_users)
# max_complete = top_users[0][1]
# print({k: v for k, v in todos_by_user.items() if v == max_complete})
# max_complete = top_users[0][1]
# print(max_complete)
# users = []
#
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_users = ' and '.join(users)
# s = "s" if len(users) > 1 else ''
# print(f'User{s} {max_users} completed {max_complete} TODOs ')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data_file.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)
#
# with open('filtered_data_file.json', 'r') as f:
#     data = json.load(f)
#     print(data)

# csv (Comma Separated Values) - переменные разделенные запятыми

import csv

# with open('data.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             print(f'    {row[0]} - {row[1]}. Родился в {row[2]} году')
#         count += 1
#     print(f'Всего в файле {count} строки')

# with open('data.csv', 'r') as r_file:
#     file_reader = csv.DictReader(r_file, delimiter=';')
#     count = 0
#     for row in file_reader:
#
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#
#         print(f"    {row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году")
#         count += 1
#     print(f'Всего в файле {count} строки')


# with open('student.csv', mode='w')as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_sv.csv', mode='w')as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_sv.csv') as f:
#     print(f.read())

# with open('stud.csv', mode='w') as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'Имя': 'Саша', 'Возраст': '6'})
#     file_writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
#     file_writer.writerow({'Имя': 'Вова', 'Возраст': '14'})

data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
    writer.writeheader()
    for d in data:
        writer.writerow(d)


