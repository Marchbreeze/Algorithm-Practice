'''
<1753. 최단경로>
골드4
https://www.acmicpc.net/problem/1753
'''
import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

# 그래프 간선의 각 시작점 별 목적지와 가중치 저장
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))

# 각 정점의 최단거리 기록할 테이블 설정 (모두 최고값)
distance = [int(1e9)] * (v+1)
distance[start] = 0

# 우선순위큐 설정
q = []
heapq.heappush(q, (0, start))

while q:
    # 가장 짧은 노드 정보 꺼내기
    dist, now = heapq.heappop(q)

    # 이미 적은 시간으로 방문한 적 있으면 무시
    if (distance[now] < dist):
        continue

    # 출발 가능한 간선 확인
    for edge in graph[now]:
        # 더 최단거리인 경우 교체 및 큐 추가
        cost = dist + edge[1]
        if (cost < distance[edge[0]]):
            distance[edge[0]] = cost
            heapq.heappush(q, (cost, edge[0]))

# 시작점에서 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,v+1):
    if (distance[i] == int(1e9)):
        print("INF")
    else:
        print(distance[i])
