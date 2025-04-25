'''
<2294. 동전 2>
골드5
https://www.acmicpc.net/problem/2294
'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 가치합의 최소 개수 저장하는 dp
dp = [10001] * (k+1)

for c in coins:
    for i in range(c,k+1):
        if dp[i]>0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])