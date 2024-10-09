'''
<7569. 토마토>
골드5
https://www.acmicpc.net/problem/7569
'''

# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 됨
# 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.
# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸xs
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력

from collections import deque

'''
3차원 리스트 설정
BFS 진행하며 일수 세기
3중for문으로 모든 1에서 시작 (n 최대 100)
끝나고 0 존재하는지 탐색 후 -1 여부 파악
'''

'''
[놓친 부분]
동시에 모든 토마토가 진행
1을 값으로 가지고 있는 배열의 위치를 큐에 담아준 후, day와 좌표를 모두 담은 BFS 시작 !!
'''

# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수, 상자의 수를 나타내는 H
m, n, h = map(int, input().split())

# 박스 설정
box = []
for k in range(h):
    layer = []
    for j in range(n):
        layer.append(list(map(int, input().split())))
    box.append(layer)

# 경계 설정
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

def out_of_bound(z,y,x):
    return z<0 or z>h-1 or y<0 or y>n-1 or x<0 or x>m-1

# BFS 설정
def bfs(k,j,i):
    day = 0
    while q:
        z, y, x, d = q.popleft()
        day = d
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if out_of_bound(nz, ny, nx) or box[nz][ny][nx] != 0:
                continue
            box[nz][ny][nx] = 1
            q.append((nz, ny, nx, d+1))
    return day

# 모든 1에 대해 탐색 후 진행
min_day = 0
q = deque()

for k in range(h):
    for j in range(n):
        for i in range(m):
            if box[k][j][i] == 1:
                q.append((k,j,i,0))
min_day = bfs(k,j,i)

# 탐색 이후 0 존재 확인
for k in range(h):
    for j in range(n):
        for i in range(m):
            if box[k][j][i] == 0:
                min_day = -1

print(min_day)