'''
<2573. 빙산>
골드4
https://www.acmicpc.net/problem/2573
'''

# 빙산의 각 부분별 높이 정보는 2차원 배열의 각 칸에 양의 정수로 저장
# 빙산 이외의 바다에 해당되는 칸에는 0이 저장
# 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어듦
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성
# 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력

from collections import deque
import copy  

'''
각 년마다 빙산 녹이고 BFS로 연결 확인
'''

'''
[놓친 부분]
매년 visited 리스트를 만들어서 관리하면 메모리 초과 발생 -> year로 불린값 대신 숫자로 관리
앞 인덱스부터 0 찾고 빼다보니, 앞 숫자가 0이 되며리면 그 지역도 고려 -> deepcopy활용
'''

# 행 N, 열 M
n, m = map(int, input().split())

# 빙산 초기값
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split())))

# 범위 확인
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def out_of_bound(y,x):
    return y<0 or x<0 or y>n-1 or x>m-1

# 빙산 녹이기
def melt_ice():
    previous = copy.deepcopy(ice)
    for y in range(n):
        for x in range(m):
            if previous[y][x] == 0:
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if out_of_bound(ny, nx):
                    continue
                if previous[ny][nx] == 0 and ice[y][x] > 0:
                    ice[y][x] -= 1

def bfs_to_find_seperate(year):
    q = deque()
    year_count = 0
    for y in range(n):
        for x in range(m):
            if ice[y][x] != 0 and visited[y][x] != year:
                q.append((y,x))
                visited[y][x] = year
                year_count += 1
                while q:
                    sy, sx = q.popleft()
                    for i in range(4):
                        ny = sy + dy[i]
                        nx = sx + dx[i]
                        if out_of_bound(ny, nx) or visited[ny][nx] == year or ice[ny][nx] == 0:
                            continue
                        q.append((ny, nx))
                        visited[ny][nx] = year
    global count
    if year_count != 0:
        count = year_count


year = 0
visited = [[0] * m for _ in range(n)]
while True:
    year += 1
    count = 0
    melt_ice()
    bfs_to_find_seperate(year)
    if count == 0:
        print(0)
        break
    if count > 1:
        print(year)
        break

