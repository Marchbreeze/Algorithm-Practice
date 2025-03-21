'''
<1149. RGB 거리>
실버1
https://www.acmicpc.net/problem/1149
'''

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 각 집의 (R, G, B)일 떄 최소비용 각각 저장하면?

n = int(input())
array = [(0,0,0)]
for _ in range(n):
    r, g, b = map(int, input().split())
    array.append((r,g,b))

dp = [(0,0,0)]
for i in range(1,n+1):
    min_r = array[i][0] + min(dp[i-1][1], dp[i-1][2])
    min_g = array[i][1] + min(dp[i-1][0], dp[i-1][2])
    min_b = array[i][2] + min(dp[i-1][0], dp[i-1][1])
    dp.append((min_r, min_g, min_b))

print(min(list(dp[n])))