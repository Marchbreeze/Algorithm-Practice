
'''
<1926. 그림>
실버1
https://www.acmicpc.net/problem/1926
'''

# 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력
# 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의
# 그림의 넓이란 그림에 포함된 1의 개

from collections import deque

# 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())

# 그림 정보 입력
pic = []
for i in range(n):
    pic.append(list(map(int, input().split())))

# 필요 결과값 설정
count = 0
area_list = []

# 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 범위 내 확인
def out_of_bound(y,x):
    return x<0 or x>m-1 or y<0 or y>n-1

# dfs 정의
def bfs(y,x):
    q = deque()
    q.append((y,x))
    pic[y][x] = 0
    area = 0
    while q:
        sy, sx = q.popleft()
        area += 1
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if out_of_bound(ny,nx) or pic[ny][nx] == 0:
                continue
            else:
                q.append((ny,nx))
                pic[ny][nx] = 0
    area_list.append(area)

# 그림 확인
for y in range(n):
    for x in range(m):
        if pic[y][x] == 1:
            count += 1
            bfs(y,x)

# 결과물 출력
print(count)
if (len(area_list) == 0):
    print(0)
else:
    print(max(area_list))