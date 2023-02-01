lst = input().split()
a, b, c, d = [int(i) for i in lst]
print(a, b, c, d)
if d > b:
    s = d - b
    price = s * c
    print(a + price)
else:
    print(a)


