nt = [int(i) for i in input().split()]
n, t = nt
flowers = [int(i) for i in input().split()]
k = int(input())
m = 0
s = flowers[-1]
for i in range(len(flowers)):
    m = flowers[k - 1]
print(m)
print(t)
if m <= t:
    res = s - 1
    print(res)
else:
    if m < s / 2:
        res = m - 1 + s - 1
        print(res)
    else:
        res = s - m + s - 1
        print(res)
