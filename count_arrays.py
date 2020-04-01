n, m = map(int, input().split())


def C(n, m):
    mm = 1
    nn = 1
    for t in range(1, min(n, m -n) + 1):
        mm *= m
        nn *= t
        m -= 1
    return mm // nn


def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * power(a, n - 1)
    elif n % 2 == 0:
        return power(a * a, n / 2)


# print(C(n, m))
# print(power(2, n - 3))
print(C(n - 1, m) * (n - 2) * power(2, n - 3))
