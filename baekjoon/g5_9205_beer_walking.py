'''
<9205. 맥주 마시면서 걸어가기>
골드5
https://www.acmicpc.net/problem/9205
'''

# 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발
# 맥주 한 박스에는 맥주가 20개
# 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 함
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있음
# 박스에 들어있는 맥주는 20병을 넘을 수 없다. 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 함
# 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이

from collections import deque

'''
거리가 100 이하인 모든 노드를 찾아서 이동해보는 BFS 진행
'''

# 테스트 개수 t
t = int(input())
for _ in range(t):
    # 편의점 개수 n
    n = int(input())

    # 좌표 입력
    arr = []
    for _ in range(n+2):
        arr.append(list(map(int, input().split())))

    # 방문 기록
    visited = [False] * (n+2)
    
    # BFS로 거리 비교 후 이동
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        visited[v] = True
        if v == n+1:
            print("happy")
            break
        for i in range(n+2):
            if visited[i] is True:
                continue
            if abs(arr[v][0] - arr[i][0]) + abs(arr[v][1] - arr[i][1]) <= 1000:
                q.append(i)
    else:
        print("sad")