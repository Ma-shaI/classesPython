import re

n = int(input())
s = input()
lst = []
reg = r'[a-d]*'
for i in range(len(s)):
    for j in range(len(s)):
        sm = s[i:len(s)-j]

        reg_s = re.findall(reg, sm)
        for j in reg_s:
            if 'a' in j and 'b' in j and 'c' in j and 'd' in j:
                lst.append(j)
try:
    print(len(min(lst, key=len)))
except ValueError:
    print(-1)