'''
< 40. 숨바꼭질 >
1~N 번 헛간중에 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다.
맵에는 총 M개의 양방향 통로가 존재한다.
술래에게서 가장 통로를 많이 거쳐야하는 헛간을 찾으시오.
(2 <= N <= 20,000, 1 <= M <= 50,000)
'''
INF = int(1e9)

# 헛간 수, 통로 수 입력
n, m = map(int, input().split())

# 통로 정보 입력 (0 ~ N-1번으로 변환)
road = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a-1].append(b-1)
    road[b-1].append(a-1)

# 각 테이블 초기화하기
distance = [INF] * (n)
distance[0] = 0

# 모든 최단 경로 찾기
for i in range(n):
    for j in range(len(road[i])):
        distance[road[i][j]] = min(distance[road[i][j]], distance[i]+1)

# 결과 출력
result = 0
for i in range(n):
    result = max(result, distance[i])
print("length : ",result)
print("house : ",distance.index(result)+1)
