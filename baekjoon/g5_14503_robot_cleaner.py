'''
<14503. 로봇 청소기>
골드5
https://www.acmicpc.net/problem/14503
'''

'''
로봇 청소기가 있는 방은 NxM 크기의 직사각형으로 나타낼 수 있으며, 1X1 크기의 정사각형 칸
처음에 빈 칸은 전부 청소되지 않은 상태

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로 90도 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.
'''

# 방 크기 N, M
n, m = map(int, input().split())

# 로봇 좌표, 방향 (0북 1동 2남 3서)
y, x, d = map(int, input().split())

dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 방 구성 (-1 청소O, 0 청소X, 1 벽)
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 청소
count = 0
while True:
    # 1. 해당 칸 청소
    if room[y][x] == 0:
        room[y][x] = -1
        count += 1
    # 방향 빈칸 확인
    for i in range(1,5):
        ny = y + dy[(d+3*i)%4]
        nx = x + dx[(d+3*i)%4]
        # 3. 빈칸이 있는경우
        if room[ny][nx] == 0:
            y, x, d = ny, nx, (d+3*i)%4
            break
    # 2. 빈칸이 없는경우
    else:
        y = y + dy[(d+2)%4]
        x = x + dx[(d+2)%4]
        if room[y][x] == 1:
            print(count)
            break