n = int(input())
s = [int(i) for i in input().split()]
k = int(input())
lst = set()
count = 0
while n >= k:
    for i in range(len(s)):
        lst.add(tuple(s[i:n]))
    n -= 1

for i in lst:
    if len(set(i)) >=k:
        count+=1

print(count)