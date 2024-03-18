---

## 간단한 다익스트라 알고리즘

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
    
- 구현 :
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
        

## 개선된 다익스트라 알고리즘

- 복잡도 : `O(ElogV)` - E : 간선 개수, V : 노드 개수
    - 기존 = 매번 최단거리 테이블을 탐색하여 가장 짧은 노드 찾는 데에만 O(V) 시간을 소요함
    - 이 방법을 선형 탐색이 아닌 다른 방법을 활용해보기

- `힙` 자료구조 (Heap)
    - `우선순위 큐` 구현 - 우선순위가 가장 높은 데이터를 가장 먼저 삭제함
        - 최소 힙 : 값이 낮은 데이터 우선 삭제
        - 최대 힙 : 값이 높은 데이터 우선 삭제 → 구현하려면 값에 (-) 붙여서 최소 힙 활용
    - 파이썬 : `heapq` 라이브러리
        - 튜플 형태로 우선순위 큐에 삽입 - 첫번째 원소를 기준으로 우선순위 큐 구성됨
    
- 원리 :
    1. 출발 노드 설정
        
        ![2024-03-18_16-04-11.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/1d552683-edb0-437c-81ed-01f56e302e58/2024-03-18_16-04-11.jpg)
        
        ![2024-03-18_16-04-25.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/198413a7-2669-4f08-b5c4-32df7b286613/2024-03-18_16-04-25.jpg)
        
    2. 우선순위 큐에서 짧은 노드 꺼내기
        - 이미 처리한 적 있는 경우 무시
        - 처리한 적 없는 경우 기존 경로의 길이와 비교해서 더 짧은 경로를 갱신
        
        ![2024-03-18_16-06-54.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/d2982610-880c-4373-828b-5d153fa615f6/2024-03-18_16-06-54.jpg)
        
    3. 반복
        
        ![2024-03-18_16-07-46.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/85c5e070-417c-488c-8f8b-3784c08bb6e3/2024-03-18_16-07-46.jpg)
        
        …
        
        ![2024-03-18_16-08-28.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/fd232241-b67e-47fb-9e6c-ea6fc5896cc6/2024-03-18_16-08-28.jpg)
        
        ![2024-03-18_16-08-37.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/af28b821-4369-4268-8dda-998efd783dd0/2024-03-18_16-08-37.jpg)
        
    - 코드 :
        
        ```python
        import heapq
        import sys
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
        
        # 모든 노드로 가기 위한 최단 거리 출력
        dijkstra(start)
        for i in range(1, n+1):
        		if (distance[i] == INF):
        				print("INFINITY")
        		else:
        				print(distance[i])
        ```
        

## 플로이드 워셜 알고리즘

- `모든 지점에서 다른 모든 지점까지의 최단 경로`를 모두 구해야하는 경우 활용
- `2차원 리스트`에 최단 거리 정보 저장
- DP - N번의 단계를 반복하며 `점화식`에 맞게 2차원 리스트 갱신 진행
- 복잡도 : `O(N^3)`

- 방법 :
    - 한개의 노드를 선택하고, N-1개의 노드 중에서 서로 다른 노드 (A, B) 쌍 선택
    - A → 노드 → B 로 가는 비용을 확인한 후 최단 거리 갱신
    - N-1P2 개의 쌍을 단계마다 반복해서 확인
    - 점화식 :
        
        ![2024-03-18_19-03-00.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/67fc6aaa-10ab-4157-a287-36a96cc66804/2024-03-18_19-03-00.jpg)
        
        = A에서 B로 가는 최소 비용 & A에서 K를 거쳐 B로 가는 비용을 비교해서 최소 값으로 갱신
        

- 사진 예시 :
    
    ![2024-03-18_19-04-46.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/2416c869-ea66-4f42-9b77-aec8c2a8803d/2024-03-18_19-04-46.jpg)
    
    1. 2차원 테이블로 간선 정보 기입
        
        ![2024-03-18_19-06-20.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/55232789-87a7-42c2-9882-d61816ed5d0d/2024-03-18_19-06-20.jpg)
        
    2. 특정 노드를 거쳐 가는 경우 모두 고려
        - 3P2 (6) 개의 경우에 대해서 각 노드들 확인
            - 1번 노드의 경우 : D23, D32, D24, D42, D34, D43 의 경우 확인 후 만족 시 교체
            - 2번 노드의 경우 : …
        - 모든 노드에 대해 반복 후 결과 도출
        
        ![2024-03-18_19-14-13.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/de72ab66-a5b6-4602-979a-42bfbe52c7c6/2024-03-18_19-14-13.jpg)
        
    
- 코드 구현 :
    
    ```python
    INF = int(1e9)
    
    # 노드, 간선 개수 입력받기
    n, m = map(int, input().split())
    
    # 2차원 리스트 만들고 초기화
    graph = [[INF] * (n+1) for I in range(n+1)]
    
    # 자기 자신 비용 0으로 설정
    for a in range(1, n+1):
    		for b in range(1, n+1):
    				if (a==b):
    						graph[a][b] = 0
    
    # 각 간선 비용 설정
    for _ in range(m):
    		a,b,c = map(int, input().split())
    		graph[a][b] = c
    
    # 점화식 따라서 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1):
    		for a in range(1, n+1):
    				for b in range(1, n+1):
    						graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    
    # 결과 출력
    for a in range(1, n+1):
    		for b in range(1, n+1):
    				if (graph[a][b] == INF):
    						print("INFINITY", end=" ")
    				else:
    						print(distance[i], end=" ")
    		print()
    ```
    

## 2. 방문 판매원 문제

<aside>
❔ 방문 판매원 A는 1번 회사에서 K번 회사를 지나 X번 회사에 도착하려고 한다.

1번부터 N번 회사가 존재하며, 특정 회사끼리는 총 M개의 도로를 통해서 양방향으로 연결되어 있으며, 모두 1만큼의 시간이 소요된다.
(1 ≤ N, M ≤ 100)

방문 판매원이 이동하는 최소 시간을 구하시오.

</aside>

- 예시 :
    
    ![2024-03-18_21-04-07.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/2ae84879-bef7-4016-8046-648f10aa0925/2024-03-18_21-04-07.jpg)
    
    ![2024-03-18_21-03-16.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/fef33cf2-a6c1-4081-a898-47fbc7bf918d/2024-03-18_21-03-16.jpg)
    
    - K=5, X=4인 경우 : 1-3-5-4로 최소 이동 시간은 3이다.
    
- 풀이 :
    - N의 범위가 100 이하로 매우 한정적이므로, `플로이드 워셜 알고리즘`을 활용할 수 있다.
    
    ```python
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
    ```
    

## 3. 전보 전달 가능한 도시 문제

<aside>
❔ N개의 도시, M개의 통로가 존재하는 나라에서, 단방향의 통로가 존재하는 경우 전보를 전송할 수 있으며, 일정 시간이 소요된다.
(1 ≤ N ≤ 30,000, 1 ≤ M ≤ 200,000)
(1 ≤ 소요 시간 ≤ 1,000)

도시 C에서 최대한 많은 도시로 전보를 보내려고 한다. 각 도시의 번호와 통로의 정보가 주어졌을 때, 전보를 받을 수 있는 도시는 총 몇개이며, 도시들이 모두 전보를 받는데까지 걸리는 시간을 계산하시오.

</aside>

- 풀이 :
    - 한 도시에서 다른 도시까지의 최단 거리 문제 : `다익스트라` 활용
    - N, M의 범위가 크기때문에 `우선순위큐`를 활용해야 함
    
    ```python
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
    ```