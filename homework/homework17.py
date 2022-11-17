def nums_bin(n):
    num_bin = ''
    m = 0
    if n > 0:
        m = n
    else:
        m = abs(n)

    while m > 0:
        num_bin += str(m % 2)
        m //= 2

    return num_bin[::-1]


print("Введите положительное число, а я переведу его в десятичное. \nДля того чтобы закончить введите 0")

while True:
    num = int(input('Введите положительное число '))
    if num > 0:
        print(nums_bin(num))
    elif num < 0:
        print('-', end='')
        print(nums_bin(num))
    else:
        print('Вы вышли')
        break
