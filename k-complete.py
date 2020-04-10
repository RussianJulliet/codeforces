from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().split())
    s = stdin.readline()
    cnt = [[0 for i in range(26)] for j in range((k + 1) // 2)]
    for i in range(n):
        cnt[min(i % k, k - i % k - 1)][ord(s[i]) - ord('a')] += 1
    ans = 0
    for i in range(k // 2):
        ans += 2 * n // k - max(cnt[i])
    if k % 2 == 1:
        ans += n // k - max(cnt[k // 2])
    print(ans)