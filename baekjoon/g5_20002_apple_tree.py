'''
<20002. 사과나무>
골드5
https://www.acmicpc.net/problem/20002
'''

n = int(input())
value = [list(map(int, input().split())) for _ in range(n)]

# 누적합
acc = [[0] * (n+1) for _ in range(n+1)]
for y in range(1,n+1):
    for x in range(1,n+1):
        acc[y][x] = value[y-1][x-1] + acc[y][x-1] + acc[y-1][x] - acc[y-1][x-1]

# 정사각형
answer = 0
max_profit= acc[1][1]
for k in range(n):
    for i in range(1,n-k+1):
        for j in range(1,n-k+1):
            cur_profit = acc[i+k][j+k] - acc[i-1][j+k] - acc[i+k][j-1] + acc[i-1][j-1]
            if max_profit < cur_profit:
                max_profit = cur_profit

print(max_profit)