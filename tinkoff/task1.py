import math

a = int(input('->'))


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def print_n(num, count=0):
    if num == 2 or is_prime(num):
        count += num - 1
    else:
        return print_n(num // 2, count + 1)
    return count


if a % 2 == 0:
    print(print_n(a))
else:
    n = round(a * 2 / 3)
    k = a - n

    m = n - k
    s = print_n(k) + print_n(m)
    print(s + 2)
