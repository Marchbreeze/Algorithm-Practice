---

## 다익스트라 알고리즘

- 그래프에서 여러 개의 노드가 있을 때, 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- `음의 간선이 없을 때` 정상 작동함
- 실제 GPS 소프트웨어의 기본 알고리즘
- `그리디` 알고리즘으로 분류됨 - 매번 최저비용 노드를 선택해서 임의의 과정 반복함
- 각 노드에 대한 현재까지의 최단 거리 정보를 항상 `1차원 리스트에 저장`하며 `계속 갱신`

- 원리 :
    1. 출발 노드 설정
    2. 최단 거리 테이블 초기화
    3. 미방문 노드 중 최단거리 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블 갱신
    5. 3,4 반복

- 그림으로의 이해 :
    
    ![파이썬 : 무한 = 10억으로 설정 `int(1e9)`](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/edc2a152-28bf-4e84-922d-3f5fb542f1b6/2024-03-14_17-08-29.jpg)
    
    파이썬 : 무한 = 10억으로 설정 `int(1e9)`
    
    ![2024-03-14_17-08-55.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/8264e16b-1ac5-4320-9f9e-be66b4f8d39f/2024-03-14_17-08-55.jpg)
    
    ![2024-03-14_17-09-12.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/c3c31679-2383-471f-beac-9e1b59aa62ce/2024-03-14_17-09-12.jpg)
    
    ![2024-03-14_17-09-59.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/1b941fd5-e169-4a8e-8fa7-c0068b98473a/2024-03-14_17-09-59.jpg)
    
    ![2024-03-14_17-10-10.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/f527c280-f747-45a6-807b-42e2d037cbbd/2024-03-14_17-10-10.jpg)
    
    … 모두 방문까지 반복…
    
    ![2024-03-14_17-10-33.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/5330d0d1-e2d4-4cd9-aa20-d819557a10c3/2024-03-14_17-10-33.jpg)
    

### 구현 - 간단한 다익스트라 알고리즘

- 복잡도 : `O(V^2)` - V : 노드 개수
- 노드 개수가 `5000개 이하`인 경우 일반적으로 수행 가능
- 단계마다 `방문하지 않은 노드 중 최단 거리가 가장 짧은 노드`를 선택하여 모든 원소들을 `순차 탐색`
    
    ```python
    import sys
    input = sys.stdin.readline
    INF = int(1e9)
    
    # 노드, 간선 개수 입력받기
    n, m = map(int, input().split())
    
    # 시작 노드 입력받기
    start = int(input())
    
    # 각 테이블 초기화하기
    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)
    
    # 모든 간선 정보 입력받기
    for _ in range(m):
    		# a번 노드에서 b번 노드로 가는 비용이 c일때
    		a, b, c = map(int, input().split())
    		graph[a].append((b,c))
    
    # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 번호를 반환 (다음 탐색으로 선정하기 위해)
    def get_smallest_node():
    		min_value = INF
    		index - 0
    		for i in range(1, n+1):
    				if (distance[i] < min_value and not visited[i]):
    						min_value = distance[i]
    						index = i
    		return index
    	
    # 다익스트라 진행
    def dijkstra(start):
    		# 시작 노드에 대해서 정보 입력
    		distance[start] = 0
    		visited[start] = True
    		for i in graph[start]:
    				distance[i[0]] = i[1]
    		# 나머지 노드 반복
    		for i in range(n-1):
    				# 최단거리 가장 짧은 노드 처리
    				now = get_smallest_node()
    				visited[now] = True
    				for j in graph[now]:
    						cost = distance[now] + j[1]
    						if (cost < distance[j[0]]):
    								distance[j[0]] = cost
    
    # 모든 노드로 가기 위한 최단 거리 출력
    dijkstra(start)
    for i in range(1, n+1):
    		if (distance[i] == INF):
    				print("INFINITY")
    		else:
    				print(distance[i])
                    
    ```