'''
<2606. 바이러스>
실버3
https://www.acmicpc.net/problem/2606
'''

# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성

# 컴퓨터 개수 n
n = int(input())

# 노드 개수 m
m = int(input())

# 노드 저장
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs로 방문 기록
visited = [0] * (n+1)

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

dfs(1)
print(sum(visited)-1)