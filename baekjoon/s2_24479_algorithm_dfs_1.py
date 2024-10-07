'''
<24479. 알고리즘 수업 - 깊이 우선 탐색 1>
실버2
https://www.acmicpc.net/problem/24479
'''

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1
# 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력

import sys
sys.setrecursionlimit(10 ** 5)

# 정점 수 n, 간선 수 m, 시작 정점 r
n, m, r = map(int, input().split())

# 연결 기록
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 진헹
visited = [0] * (n+1)
count = 0
def dfs(i):
    global count
    count += 1
    visited[i] = count
    for j in sorted(graph[i]):
        if visited[j] == 0:
            dfs(j)

dfs(r)
for i in range(1,n+1):
    print(visited[i])