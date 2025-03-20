'''
<1504. 특정한 최단 경로>
골드4
https://www.acmicpc.net/problem/1504
'''

import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

mid1, mid2 = map(int, input().split())

def min_distances(start):
    distance = [int(1e9)] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for edge in graph[now]:
            cost = dist + edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(q, (cost, edge[0]))

    return distance

from_start = min_distances(1)
from_mid1 = min_distances(mid1)
from_mid2 = min_distances(mid2)

min_dist = min(from_start[mid1] + from_mid1[mid2] + from_mid2[n], from_start[mid2] + from_mid2[mid1] + from_mid1[n])
if min_dist >= int(1e9):
    print(-1)
else:
    print(min_dist)