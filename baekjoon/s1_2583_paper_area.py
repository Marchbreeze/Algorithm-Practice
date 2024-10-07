'''
<2583. 영역 구하기>
실버1
https://www.acmicpc.net/problem/2583
'''

# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이
# 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역

from collections import deque

# 숫자 입력
m, n, k = map(int, input().split())

# 종이 세팅
arr = [[1] * n for _ in range(m)]

# 그림 세팅
for i in range(k):
    lux, luy, rdx, rdy = map(int, input().split())
    rdx -= 1
    rdy -= 1
    for y in range(luy,rdy+1):
        for x in range(lux,rdx+1):
            arr[y][x] = 0

#      ↑  ←  ↓  →
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > m-1

# bfs 진행
area_list = []
for y in range(m):
    for x in range(n):
        if arr[y][x] == 1:
            q = deque()
            q.append((y,x))
            arr[y][x] = 0
            area = 1
            while q:
                sy, sx = q.popleft()
                for i in range(4):
                    ny = sy + dy[i]
                    nx = sx + dx[i]
                    if out_of_range(ny,nx):
                        continue
                    elif arr[ny][nx] == 1:
                        q.append((ny,nx))
                        arr[ny][nx] = 0
                        area += 1
            area_list.append(area)

area_list.sort()
print(len(area_list))
print(' '.join(map(str, area_list)))