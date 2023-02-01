n = int(input())
lst = [int(i) for i in input().split()]
t = []
for i in range(len(lst)):

    if (lst[i] % 2 == 0 and (i+1) % 2 == 0) or (lst[i] % 2 != 0 and (i+1) % 2 != 0):
        continue
    else:
        t.append(i+1)

print(' '.join(map(str, t)) if len(t) == 2 else ' '.join(map(str, [-1, -1])))

