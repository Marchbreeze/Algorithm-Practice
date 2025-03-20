'''
<2206. 벽 부수고 이동하기>
골드3
https://www.acmicpc.net/problem/2206
'''

# (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동 (벽 = 1로 표시)
# 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))

    while q:
        a, b, break_count = q.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][break_count]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and break_count == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                q.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][break_count] == 0:
                visited[nx][ny][break_count] = visited[a][b][break_count] + 1
                q.append((nx, ny, break_count))
    return -1


print(bfs(0, 0, 0))
