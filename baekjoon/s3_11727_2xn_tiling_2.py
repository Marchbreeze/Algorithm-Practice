'''
<11727. 2xn 타일링 2>
실버3
https://www.acmicpc.net/problem/11727
'''

n = int(input())

dp = [0,1,3,5]
if (n > 3):
    dp += [0] * (n-3)

for i in range(4, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[n])