'''
<14501. 퇴사>
실버3
https://www.acmicpc.net/problem/14501
'''

# 상담원, 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담
# 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

'''
DP 문제
1일차 3일 10 -> 3~7일차 10 설정
'''

# N (N<=15)
n = int(input())

# 상담표 추가
arr = [(0,0)]
for i in range(n):
    t,p = map(int, input().split())
    arr.append((t,p))

# DP 테이블 설정 (1일차부터)
dp = [0] * (n+1)

for i in range(1,n+1):
    t, p = arr[i]
    if i+t-1 > n:
        continue
    for j in range(i+t-1,n+1):
        if dp[i-1] + p > dp[j]:
            dp[j] = dp[i-1] + p

print(dp[n])