'''
<11404. 플로이드>
골드4
https://www.acmicpc.net/problem/11404
'''

# 도시, 버스 입력
n = int(input())
m = int(input())

# 비용 입력
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(cost, graph[start][end])

# 자기 자신 비용 0
for a in range(1, n+1):
    graph[a][a] = 0

# a-b, a-k-b 비교하는 점화식을 삼중 반복문으로 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for row in graph[1:]:
    for i in range(1,n+1):
        if (row[i] >= int(1e9)):
            row[i] = 0
    print(' '.join(map(str, row[1:])))