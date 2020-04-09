primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def getprime(x):
    for i in range(2, x):
        if x % i == 0:
            return i
    return -1


t = int(input())
for s in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    used = [False for i in range(11)]
    clr = []
    for i in range(n):
        x = primes.index(getprime(numbers[i]))
        used[x] = True
        clr.append(x)
    cnt = 0
    num = []
    for i in range(11):
        num.append(cnt)
        if used[i]:
            cnt += 1
    print(cnt)
    for i in range(n):
        x = primes.index(getprime(numbers[i]))
        print(num[x] + 1, end=" ")
    print()


