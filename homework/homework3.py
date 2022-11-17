n = int(input('Введите начало диапазона (включительно): '))
m = int(input('Введите конец диапазона (включительно): '))
start = n if n < m else m
finish = m if n < m else n
count = 0
while start <= finish:
    count += start if start % 2 != 0 else 0
    start += 1
print('Сумма целых нечетных чисел:', count)
