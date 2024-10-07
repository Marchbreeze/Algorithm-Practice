'''
<2468. 안전 영역>
실버1
https://www.acmicpc.net/problem/2468
'''

# 어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
# 물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역
# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산

from collections import deque

# 영역 크기
n = int(input())

# 지형
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

#      ↑  ←  ↓  →
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > n-1

# 모든 높이 비교 (1~100)
height_list = []

for h in range(101):

    # 방문여부 확인
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    # bfs 진행
    for y in range(n):
        for x in range(n):
            if visited[y][x] is False and area[y][x] > h:
                q = deque()
                q.append((y,x))
                while q:
                    sy, sx = q.popleft()
                    for i in range(4):
                        ny = sy + dy[i]
                        nx = sx + dx[i]
                        if out_of_range(ny, nx) or visited[ny][nx] or area[ny][nx] <= h:
                            continue
                        q.append((ny,nx))
                        visited[ny][nx] = True
                count += 1
   
    height_list.append(count)

print(max(height_list))
                