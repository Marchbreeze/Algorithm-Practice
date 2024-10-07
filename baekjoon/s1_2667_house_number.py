'''
<2667. 단지 번호 붙이기>
실버1
https://www.acmicpc.net/problem/2667
'''

# 정사각형 모양의 지도, 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타냄
# 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 함

from collections import deque

# 숫자 입력
n = int(input())

# 지도 세팅
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

#      ↑  ←  ↓  →
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > n-1

# bfs 진행
area_list = []
for y in range(n):
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
house = len(area_list)
print(house)
for i in range(house):
    print(area_list[i])