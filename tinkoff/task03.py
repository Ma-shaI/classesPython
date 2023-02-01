n = int(input())
set_l = {int(i) for i in input().split()}
m = int(input())
new_set = set()

request = []
for i in range(m):
    request.append([int(i) for i in input().split()])

for i in request:
    match i[0]:
        case 0:
            print('Yes' if i[1] in set_l else 'No')
        case 1:
            for j in set_l:
                new_set.add(j + i[1])
            set_l = new_set
        case 2:
            set_l.add(i[1])
        case 3:
            set_l.remove(i[1])
