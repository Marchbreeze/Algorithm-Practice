'''
<11725. 트리의 부모 찾기>
실버2
https://www.acmicpc.net/problem/11725
'''

# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력

from collections import deque

# 노드 개수 n
n = int(input())
graph = [[] for _ in range(n+1)]

# 간선 추가
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

parent = [-1] * (n+1)
parent[1] = 0

q = deque()
q.append(1)
while q:
    i = q.popleft()
    for j in graph[i]:
        if parent[j] == -1:
            parent[j] = i
            q.append(j)

for i in parent[2:]:
    print(i)