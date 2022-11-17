a = 1
b = 2
print("a:", a)
print("b:", b)
# a, b = b, a
# c = a
# a = b
# b = c
a = a + b
b = a - b
a = a - b
print("a:", a)
print("b:", b)

a, b, c = 5, 7, 3
print("Сумма:", a + b + c)
print("Произведение:", a * b * c)
print("Среднее арифмeтическое: " + str((a + b + c) / 3))
