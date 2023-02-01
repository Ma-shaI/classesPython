n = int(input())
s = input()
lst = [i for i in s]
if n % 2 != 0:
    print('NO')

else:
    a = [i for i in s[:(n // 2)]]
    b = [i for i in s[(n // 2):]]
    if a == b:
        print('YES')

    else:
        c = []
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] != b[j] and i == j:
                    c.append(i)
        if len(c) == 2:
            a[c[0]], a[c[1]] = a[c[1]], a[c[0]]
            if a == b:
                print('YES')
        else:
            print('NO')
