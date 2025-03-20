'''
<4485. 녹색 옷 입은 애가 젤다지?>
골드4
https://www.acmicpc.net/problem/4485
'''
import heapq

dx = [0,0,-1,1]
dy = [1,-1,0,0]

t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break

    array = [list(map(int, input().split())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    distance[0][0] = array[0][0]

    q = []
    heapq.heappush(q, (0, 0, array[0][0]))
    while q:
        a, b, dist = heapq.heappop(q)
        if dist > distance[a][b]:
            continue
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if (na<0 or na>n-1 or nb<0 or nb>n-1):
                continue
            cost = dist + array[na][nb]
            if (cost < distance[na][nb]):
                distance[na][nb] = cost
                heapq.heappush(q, (na, nb, cost))
    
    print(f'Problem {t}: {distance[n-1][n-1]}')
    