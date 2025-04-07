'''
<14940. 쉬운 최단거리>
실버1
https://www.acmicpc.net/problem/14940
'''
from collections import deque

n, m = map(int, input().split())
dis = [[-1] * m for _ in range(n)]
array = []

q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 0:
            dis[i][j] = 0
        if row[j] == 2:
            dis[i][j] = 0
            q.append((i,j,0))
    array.append(row)

while q:
    y, x, count = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>m-1 or ny<0 or ny>n-1:
            continue
        if dis[ny][nx] >= 0:
            continue
        dis[ny][nx] = count + 1
        q.append((ny, nx, count + 1))

for row in dis:
    print(' '.join(map(str, row)))