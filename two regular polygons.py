count_figures = int(input())
for i in range(count_figures):
    n, m = map(int, input().split())
    if n % m == 0:
        print('YES')
    else:
        print('NO')
