'''
<12865. 평범한 배낭>
골드5
https://www.acmicpc.net/problem/12865
'''

n, k = map(int, input().split())
array = []
for _ in range(n):
    w, v = map(int, input().split())
    array.append((w,v))

dp = [0] * (k+1)

for item in array:
    w, v = item
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])
