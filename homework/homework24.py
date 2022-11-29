f = open('text.txt', 'w')
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
f.close()


f = open('text.txt', 'r')
read_line = f.readlines()
f.close()
print(read_line)
pos1 = int(input("Введите 1ый индекс: "))
pos2 = int(input('Введите 2ой индекс: '))
if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
     print('Такой строки нет')
print(read_line)
f = open('text.txt', 'w')
f.writelines(read_line)
f.close()
