n = [int(i) for i in input().split()]
if n == sorted(n) or n == sorted(n, reverse=True):
    print('YES')
else:
    print('NO')