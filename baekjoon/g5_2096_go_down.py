'''
<2096. 내려가기>
골드5
https://www.acmicpc.net/problem/2096
'''

n = int(input())
# 첫 번째 행 읽기: 최대, 최소 값이 동일하게 초기화됨
first = list(map(int, input().split()))
max_dp = first[:]  
min_dp = first[:]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    new_max_dp = [0, 0, 0]
    new_min_dp = [0, 0, 0]
    
    new_max_dp[0] = a + max(max_dp[0], max_dp[1])
    new_max_dp[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
    new_max_dp[2] = c + max(max_dp[1], max_dp[2])
    
    new_min_dp[0] = a + min(min_dp[0], min_dp[1])
    new_min_dp[1] = b + min(min_dp[0], min_dp[1], min_dp[2])
    new_min_dp[2] = c + min(min_dp[1], min_dp[2])
    
    max_dp, min_dp = new_max_dp, new_min_dp

print(max(max_dp), min(min_dp))