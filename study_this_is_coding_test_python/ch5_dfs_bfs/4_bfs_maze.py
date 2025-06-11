from collections import deque

# N, M 입력받기
n, m = map(int, input().split())

# 미로 맵 정보 입력받기
maze = []
for i in range(n) :
    maze.append(list(map(int, input())))

# 상하좌우 방향 정의
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

# BFS 구현
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    # 큐가 모두 빌 때까지 반복
    while queue :
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m) :
                continue
            if (maze[nx][ny] == 0) :
                continue
            # 조건을 만족하는 해당 노드를 처음 방문하는 경우 최단 거리로 기록
            if (maze[nx][ny] == 1) :
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0,0))