n, m, p = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
for i in range(n):
    if arr_1[i] % p != 0:
        d1 = i
        break
for j in range(m):
    if arr_2[j] % p != 0:
        d2 = j
        break
print(d1 + d2)



