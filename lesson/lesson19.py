# Работа с файлами

# f = open('text.txt')
# # print(f)
# # print(*f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# f= open('text.txt', 'r')
# print(f.read(3))
# print(f.read(3))
# f.close()

# f = open('text.txt','r')
# try:
#     print(f.read())
# finally:
#     f.close()
#
# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('test.txt', 'r')
# print(f.readlines(16))
#
# f.close()

# f = open('test.txt', 'r')
# for line in f:
#     print(line, end='')
# f.close()

# f = open('test.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w', encoding='utf-8')
# f.write(str('Привет\nМир!'))
# f.close()
#
# f = open('xyz.txt', 'a')
# # print(f.write(str('\nNew Text')))
# lines=['Line1', 'Line2', 'Line3']
# f.writelines(lines)
# f.close()

#
# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i - 1) + '\t' for i in range(1, 20)]
# print(lst)
# # f.writelines(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменить строку в списке;\n':
#         read_file[i] = 'Hello world!\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text3.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# n = int(input("Введите индекс: "))
# f = open('text3.txt', 'r')
# read_line = f.readlines()
# f.close()
#
# if 0 <= n < len(read_line):
#     read_line.pop(n)
# else:
#      print('Такой строки нет')
#
# f = open('text3.txt', 'w')
# f.writelines(read_line)
# f.close()


# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))  # 20
# print(f.seek(3))  # 3
# print(f.write('--new string--'))  # 14
# print(f.tell())  # 17
#
# f.close()

# f = open('text.txt', 'a')
# print(f.write('\nI am learning Python\n'))  # 20
# print(f.seek(3))  # 3
# print(f.write('--new string--'))  # 14
# print(f.tell())  # 17
#
# f.close()

# f = open('text4.txt', 'wb')
# print(f.write(b'\nI am learning Python\n'))  # 20
# # print(f.seek(3))  # 3
# # print(f.write('--new string--'))  # 14
# # print(f.tell())  # 17
#
# f.close()