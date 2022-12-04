file1 = 'file1.txt'
file2 = 'file2.txt'
file3 = 'file3.txt'


with open(file1, 'w') as f1, open(file2, 'w') as f2:
    f1.write('Текст для первого файла\n')
    f2.write('Текст для второго файла\n')

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
    fr1= f1.read()
    fr2 = f2.read()
    text = fr1 + fr2
    f3.write(text)
