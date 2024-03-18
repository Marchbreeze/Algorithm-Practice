import heapq
import sys

# 시작 전 정의
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 입력받기
start = int(input())

# 각 테이블 초기화하기
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c일때
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 다익스트라 진행
def dijkstra(start):
    q = []
    # 시작 노드에 대해서 정보 입력
    heapq.headpush(q, (0,start))
    distance[start] = 0
    # 큐가 비어있지 않다면
    while q:
        # 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 방문한 적 있으면 무시
        if distance[now] < dist :
            continue
        # 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if (cost < distance[i[0]]):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수 & 거리 총합 (시작 노드 제외)
count = -1
max_distance = 0
for d in distance:
    if (d != INF):
        count += 1
        max_distance = max(max_distance, d)

print(count, max_distance)