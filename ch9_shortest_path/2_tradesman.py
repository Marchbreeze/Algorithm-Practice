
# 무한 정의
INF = int(1e9)

# 노드, 간선 개수 입력
n,m = map(int, input().split())

# 플로이드 워셜 수행 위한 2차원 리스트 생성 및 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신 비용 0 설정
for a in range(1, n+1):
    for b in range(1, n+1):
        if (a==b) :
            graph[a][b]=0

# 간선 정보 설정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 방문할 노드 정보 입력
x,k = map(int, input().split())

# 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
distance = graph[1][k]+graph[k][x]
if distance >= INF :
    print("not reachable")
else:
    print(distance)