'''
<11724. 연결 요소의 개수>
실버2
https://www.acmicpc.net/problem/11724
'''

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성

# 정점 개수 n, 간선 개수 m
n, m = map(int, input().split())

# 연결 기록
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 진행
visited = [False] * (n+1)
def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j] is False:
            dfs(j)

# 모든 정점에 대해 조사
count = 0
for i in range(1,n+1):
    if visited[i] is False:
        count += 1
        dfs(i)

print(count)