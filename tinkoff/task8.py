n = int(input())
a, b, c = map(int, input().split())
result = sum(s // c + 1 for i in range(n) for j in range(n - a * i) if (s := n - a * i - b * j - 1) >= 0)
print(result)
