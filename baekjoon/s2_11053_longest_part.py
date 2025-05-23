'''
<11053. 가장 긴 증가하는 부분 수열>
실버2
https://www.acmicpc.net/problem/11053
'''

n = int(input())
array = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))