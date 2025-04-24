'''
<2638. 치즈>
골드3
https://www.acmicpc.net/problem/2638
'''
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]

# 밖공간 -1, 치즈 1, 안공간 0

# bfs로 밖공간 모두 -1로 만들기
def check_outside():
    global array
    q = deque()
    q.append((0,0))
    visited = [[False] * m for _ in range(n)]
    while q:
        y, x = q.popleft()
        array[y][x] = -1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny<0 or ny>n-1 or nx<0 or nx>m-1:
                continue
            if visited[ny][nx] is True:
                continue
            if array[ny][nx] == 0:
                array[ny][nx] = -1
                visited[ny][nx] = True
                q.append((ny, nx))
            if array[ny][nx] == -1:
                visited[ny][nx] = True
                q.append((ny, nx))

# 치즈(1) 주위에 0 말고 -1이 2개 이상 있으면 0 만들기
count = 0
while True:
    count += 1
    has_melted = False
    check_outside()
    for y in range(n):
        for x in range(m):
            if array[y][x] == 1:
                around = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if array[ny][nx] == -1:
                        around += 1
                if around > 1:
                    array[y][x] = 0
                    has_melted = True
    if not has_melted:
        break

print(count-1)