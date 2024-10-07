'''
<2644. 촌수계산>
실버2
https://www.acmicpc.net/problem/2644
'''

# 전체 정점 수 n
n = int(input())

# 촌수 계산할 두 정점 a, b
a, b = map(int, input().split())

# 전체 간선 수 m
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

# 간선 번호
for _ in range(m):
    x, y =  map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 진행
def dfs(v):
    stack = [v]
    visited[v] = 0
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if visited[j] == -1:
                stack.append(j)
                visited[j] = visited[i] + 1

dfs(a)
print(visited[b])