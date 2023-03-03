n, m, k = [int(i) for i in input().split()]
lst = [i for i in range(n * k)]
results = [couple for couple in zip(lst[::m])]

print(len(results))