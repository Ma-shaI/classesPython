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

# with open('text5.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text5.txt', 'r') as f:
#     for line in f:
#         print(line)

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))

# print(get_line(lst))


# with open(file_name, 'r') as f:
#     nums = f.read()
#
#
# print(nums)
# lst = list(map(float, nums.split(' ')))
# print(lst)
# print(len(lst))


# def longest_words(file):
#     with open(file_name, 'r', encoding='utf8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) ==1:
#             return res[0]
#         return res
#
#
# file_name = 'res.txt'
# print(longest_words(file_name))

#
# text ='Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)
