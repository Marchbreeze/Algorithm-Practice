'''
<7576. 토마토>
골드5
https://www.acmicpc.net/problem/7576
'''

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def out_of_bound(x,y):
    return x<0 or x>n-1 or y<0 or y>m-1

q = deque()
for y in range(m):
    for x in range(n):
        if box[x][y] == 1:
            q.append((x, y, 0))

total = 0
while q:
    x, y, day = q.popleft()
    total = max(day, total)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if out_of_bound(nx, ny) or box[nx][ny] != 0:
            continue
        box[nx][ny] = 1
        q.append((nx, ny, day+1))

isFinished = True
for row in box:
    for tomato in row:
        if tomato == 0:
            isFinished = False
            print(-1)
            break
    if isFinished is False:
        break
else:
    print(total)