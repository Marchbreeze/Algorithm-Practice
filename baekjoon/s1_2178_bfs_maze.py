'''
<2178. 미로 탐색>
실버1
https://www.acmicpc.net/problem/2178
'''

# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함

from collections import deque

# N×M크기의 배열
n, m = map(int, input().split())

# 미로 입력
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 범위 내 확인
def out_of_bound(y,x):
    return x<0 or x>m-1 or y<0 or y>n-1

# 미로 시작
q = deque()
q.append((0,0))
while q:
    sy, sx = q.popleft()
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if out_of_bound(ny, nx):
            continue
        elif maze[ny][nx] == 1:
            q.append((ny, nx))
            maze[ny][nx] = maze[sy][sx] + 1

print(maze[n-1][m-1])