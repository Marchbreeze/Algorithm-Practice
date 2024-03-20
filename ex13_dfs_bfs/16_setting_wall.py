'''
< 16. 연구소 >
크기가 NxM인 연구소가 빈칸(0)과 벽(1)으로 이루어져 있으며, 벽은 칸 하나를 차지한다.
일부 칸에 바이러스(2)가 존재하며, 상하좌우로 퍼져나갈 수 있다.
벽 3개를 세워서 바이러스를 최대한 막을 수 있다.
벽을 세운 이후 바이러스가 퍼져나갈 때, 안전 영역의 최대 크기를 구하시오.
(3 <= N,M <= 8, 2 <= 바이러스수 <= 10)

--------모르겠다.........---------
'''

from collections import deque

# 연구소 크기 입력
n, m = map(int, input().split())
old_map = []
for _ in range(n):
    old_map.append(list(map(int, input().split())))

# 바이러스 위치 확인
virus = []
for x in range(n):
    for y in range(m):
        if (old_map[x][y] == 2):
            virus.append((x,y))

# 방향 설정
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 2의 상하좌우에 0 좌표 확인
need_wall = []
for v in virus:
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if (nx >= 0 and nx < n and ny >= 0 and ny < n):
            if (old_map[nx][ny] == 0):
                need_wall.append((nx, ny))

# 바이러스 퍼진 이후의 맵 확인
new_map = old_map.copy()
# 일단 앞에 3개에 벽 설정
if (len(need_wall) >= 3) :
    count = 0 
else :
    count = 3 - len(need_wall)
for i in range(3 - count):
    new_map[need_wall[i][0]][need_wall[i][1]] = 1

# bfs로 2 주위 모든 0 감염
q = deque()
for i in range(len(virus)):
    q.append(virus[i])
while q:
    now = q.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if (nx >= 0 and nx < n and ny >= 0 and ny < n):
            if (new_map[nx][ny] == 0):
                new_map[nx][ny] = 2
                q.append((new_map[nx], new_map[ny]))

# 전체 중 0 개수 세기
for x in range(n):
    for y in range(m):
        if (new_map[x][y] == 0):
            count += 1

# 결과 출력
print(count)