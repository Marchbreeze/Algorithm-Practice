'''
<9465. 스티커>
실버1
https://www.acmicpc.net/problem/9465
'''

t = int(input())
for _ in range(t):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]

    # 2행 DP배열 형성
    dp = [[0] * n for _ in range(2)]

    # 스티커 길이가 1일 경우
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # 스티커 길이가 2일 경우
    dp[0][1] = array[1][0] + array[0][1]
    dp[1][1] = array[0][0] + array[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3이상일 경우
    for i in range(2, n):
        # 메인 아이디어
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + array[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + array[1][i]

    print(max(dp[0][-1], dp[1][-1]))