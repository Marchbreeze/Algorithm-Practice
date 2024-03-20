'''
< 15. 특정 거리의 도시 찾기 >
1 ~ N 번까지의 도시와 M개의 거리 1 단방향 도로가 존재한다.
특정 도시 X에서 출발해서, 최단 거리가 K인 모든 도시의 번호를 출력하시오.
(2 <= N <= 200,000, 1 <= M <= 1,000,000, 1 <= K <= 300,000)
'''
from collections import deque

# 도시 개수, 거리 대수, 최단 거리, 출발 번호 입력
n, m, k, x = map(int, input().split())

# 단방향 거리 리스트 입력
roadList = []
for _ in range(m):
    a, b = map(int, input().split())
    roadList.append((a,b))

# 소요 시간 기록용 리스트 설정 (미방문 시 -1 설정)
timeList = [-1] * (n+1)
timeList[x] = 0
timeList[0] = 0

# bfs 설정
queue = deque()
queue.append(x)

# k번 이동할 때까지 진행함
while queue:
    now = queue.popleft()
    for road in roadList:
        if (road[0] == now and timeList[road[1]] == -1):
            timeList[road[1]] = timeList[now] + 1
            queue.append(road[1])

# 최단 시간이 k인 도시 탐색
result = []
for i in range(n+1):
    if (timeList[i] == k):
        result.append(str(i))

# 결과 출력
if (len(result) == 0):
    print(-1)
else:
    print(''.join(result))