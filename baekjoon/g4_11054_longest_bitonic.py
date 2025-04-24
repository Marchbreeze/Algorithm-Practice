'''
<11054. 가장 긴 바이토닉 부분 수열>
골드4
https://www.acmicpc.net/problem/11054
'''

n = int(input())
array = list(map(int, input().split()))
rev_array = array[::-1]

up_dp = [1] * n
down_dp = [1] * n

for idx in range(n):
    for prev in range(idx):
        if array[prev] < array[idx]:
            up_dp[idx] = max(up_dp[idx],up_dp[prev]+1)
        if rev_array[prev] < rev_array[idx]:
            down_dp[idx] = max(down_dp[idx], down_dp[prev]+1)

result = []
for i in range(n):
    result.append(up_dp[i] + down_dp[n-i-1] - 1)
print(max(result))