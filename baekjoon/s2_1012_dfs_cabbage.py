'''
<1012. 유기농 배추>
실버2
https://www.acmicpc.net/problem/1012
'''

# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅

from collections import deque

# 테스트 개수 t
t = int(input())

#      ↑  ←  ↓  →
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

def set_cab_map():
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        cx, cy = map(int, input().split())
        arr[cy][cx] = 1
    return arr

def search_cab():
    global count
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                search_near_cab_by_bfs(y,x)
                count += 1

def out_ot_range(y, x):
    return x < 0 or x > m-1 or y < 0 or y > n-1

def search_near_cab_by_bfs(iy,ix):
    q = deque()
    q.append((iy,ix))
    arr[iy][ix] = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if out_ot_range(ny,nx) or arr[ny][nx] == 0:
                continue
            else:
                q.append((ny,nx))
                arr[ny][nx] = 0

# 테스트 케이스 별 실행
for _ in range(t):
    # 배추밭 가로길이 m, 세로길이 n, 배추개수 k
    m, n, k = map(int, input().split())

    # 지도 설정
    arr = set_cab_map()

    # 배추 탐색
    count = 0
    search_cab()

    print(count)

