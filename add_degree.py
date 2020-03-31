T = int(input())
for s in range(T):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    maxPower = 1
    while maxPower <= 10000000000000000:
        maxPower *= k
    while maxPower > 0:
        s = 0
        for i in range(len(array)):
            # print(array[i])
            if array[i] >= maxPower:
                s += 1
                if s <= 1:
                    array[i] = array[i] - maxPower
        maxPower //= k
        # print(maxPower)
    # print(maxPower, array)
    if min(array) == 0 and max(array) == 0:
        print('YES')
    else:
        print('NO')


