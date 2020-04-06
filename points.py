T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    points = list(map(int, input().split()))
    summ = sum(points)
    first = points[0]
    del points[0]
    summ_new = sum(points)
    max_point = first + summ_new
    if max_point >= m:
        print(m)
    else:
        print(max_point)