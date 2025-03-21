'''
<2839. 설탕 배달>
실버4
https://www.acmicpc.net/problem/2839
'''

n = int(input())
dp = [int(1e9)] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if (dp[n] >= int(1e9)):
    print(-1)
else:
    print(dp[n])