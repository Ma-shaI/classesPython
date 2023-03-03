n = int(input())
lst = [int(i) for i in input().split()]


def form_dict(l):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct


dct = form_dict(lst)
count = 0
for key, value in dct.items():
    if value == 1:
        count += 1


def check(lst_val):
    while True:
        if dct[lst[-1]] == min(lst_val):
            del lst[-1]
        else:
            break


dct1 = form_dict(lst)
lst_value = set([i for i in dct1.values()])
if count == len(lst):
    print(count)

else:
    if max(lst_value) - min(lst_value) == 1 and len(lst_value)==2:
        while True:
            if dct[lst[-1]] == 1:
                del lst[-1]
            else:
                break
        print(len(lst))
    else:
        while len(lst_value) > 2:
            if dct[lst[-1]] == min(lst_value):
                del lst[-1]
            elif dct[lst[-1]] != min(lst_value):
                lst_value.remove(min(lst_value))
            else:
                break
        dct2 = form_dict(lst)
        lst_v = set([i for i in dct2.values()])
        if max(lst_v) - min(lst_v) == 1 and len(lst_v)==2:
            print(len(lst))
        else:
            print(-1)


