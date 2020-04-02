t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n % 2 != k % 2:
        print('NO')
    else:
        if k ** 2 > n:
            print('NO')
        else:
            print('YES')