n = int(input())
lst = []
for i in range(n-1):
    lst.append([int(i) for i in input().split()])
lst_e = [int(i) for i in input().split()]
dct = {}
for i in range(len(lst_e)):
    dct[i+1] = lst_e[i]

m =[]

for i in lst:
    if dct[i[0]] != dct[i[1]]:

        m.append(i[1])
if len(m) == 0:
    print('YES')
    print(n)
elif len(m) ==1:
    print('YES')
    print(m[0])
else:
    print('NO')