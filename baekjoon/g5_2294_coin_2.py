'''
<2294. 동전 2>
골드5
https://www.acmicpc.net/problem/2294
'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 가치합의 최소 개수 저장하는 dp
dp = [100001] * (k+1)

for c in coins:
    if c <= k:
        dp[c] = 1

for i in range(2, k+1):
    for c in coins:
        idx = i - c
        if idx > 0 and dp[idx] > 0:
            dp[i] = min(dp[i], dp[idx] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])