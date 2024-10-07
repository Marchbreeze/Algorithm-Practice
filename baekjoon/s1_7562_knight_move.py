'''
<7562. 나이트의 이동>
실버1
https://www.acmicpc.net/problem/7562
'''

from collections import deque

# 테스트 케이수 개수 t
t = int(input())

# 나이트 이동 방향
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > n-1

for i in range(t):
    # 길이, 현재칸, 목적칸 설정
    n = int(input())
    ny, nx = map(int, input().split())
    gy, gx = map(int, input().split())

    # 체스판 설정
    arr = [[-1] * n for _ in range(n)]
    arr[ny][nx] = 0

    # bfs 진행
    q = deque()
    q.append((ny,nx))
    while q:
        y, x = q.popleft()
        for i in range(8):
            sy = y + dy[i]
            sx = x + dx[i]
            if out_of_range(sy, sx):
                continue
            if arr[sy][sx] == -1 or arr[y][x] + 1 < arr[sy][sx]:
                arr[sy][sx] = arr[y][x] + 1
                q.append((sy,sx))
    
    print(arr[gy][gx])
