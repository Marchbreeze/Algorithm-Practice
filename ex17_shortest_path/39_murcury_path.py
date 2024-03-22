'''
< 39. 화성 탐사 >
N x N 크기의 2차원 공간에서, 각 칸을 지나기 위한 비용이 존재한다.
탐사기계는 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.
가장 왼쪽 위 칸인 [0][0]에서 가장 오른쪽 아래 칸인 [N-1][N-1]로 이동하는 최소 비용을 구하시오.
(2 <= N <= 125, 0 <= 비용 <= 9)
'''
INF = int(1e9)

# N 입력
n = int(input())

# 비용 입력
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

# 최소 비용 기록용 테이블
table = [[INF] * n for _ in range(n)]
table[0][0] = cost[0][0]

# 최소 비용 측정
for i in range(n):
    for j in range(n):
        if (i != 0):
            table[i][j] = min(table[i][j], table[i-1][j] + cost[i][j])
        if (j != 0):
            table[i][j] = min(table[i][j], table[i][j-1] + cost[i][j])

# 결과 출력
print(table[n-1][n-1])