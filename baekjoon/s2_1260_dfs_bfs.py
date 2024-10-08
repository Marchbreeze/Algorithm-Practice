'''
<1260. DFS와 BFS>
실버2
https://www.acmicpc.net/problem/1260
'''

from collections import deque

# 정점 N, 노드 M, 시작점 V
n, m, v = map(int, input().split())

# 간선 입력
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(v):
    order = []
    visited = [False] * (n + 1)
    stack = [v]
    while stack:
        i = stack.pop()
        if not visited[i]:
            visited[i] = True
            order.append(i)
            for j in sorted(graph[i], reverse=True):
                if not visited[j]:
                    stack.append(j)
    return order

def bfs(v):
    order = []
    visited = [False] * (n+1)
    visited[v] = True

    q = deque()
    q.append(v)
    while q:
        i = q.popleft()
        order.append(i)
        for j in sorted(graph[i]):
            if visited[j] is False:
                q.append(j)
                visited[j] = True
    return order

print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))