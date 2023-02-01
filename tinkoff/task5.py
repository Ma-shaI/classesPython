lr = [int(i) for i in input().split()]
l, r = lr
n = []
for i in range(l, r + 1):
    if len(str(i)) == 1:
        n.append(i)
    else:
        if len(set(str(i))) == 1:
            n.append(i)
print(len(n))
