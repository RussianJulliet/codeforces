n, m, p = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
for j in range(len(arr_1), max(n, m)):
    arr_1.append(0)
for j in range(len(arr_2), max(n, m)):
    arr_2.append(0)
# print(arr_1)
# print(arr_2)
for degree in range(n + m - 1):
    # print('degree:', degree)
    coeff = 0
    i = 0
    while i <= degree:
        coeff = coeff + arr_1[i] * arr_2[degree - i]
        i += 1
    # print('coeff:',coeff)
    if coeff % p != 0:
        print(degree)
        break


