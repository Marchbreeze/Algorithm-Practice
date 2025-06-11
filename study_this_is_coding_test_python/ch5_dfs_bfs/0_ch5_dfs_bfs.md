---

## 자료구조 기초

- `자료구조` : 데이터를 표현하고 관리하고 처리하기 위한 구조
- 삽입(push) & 삭제(pop)

### 스택 (Stack)

- 박스를 아래에서부터 위로 차곡차곡 쌓기
- 선입후출 구조 (FILO)
    - `stack = []`
    - `append()` & `pop()`

### 큐 (Queue)

- 놀이기구 대기줄
- 선입선출 구조 (FIFO)
    - `queue = deque()`
    - `append()` & `popleft()`
    - 일반적으로 deque() 라이브러리를 활용함 - 리스트로 필요 시 `list(queue)`로 반환

### 재귀함수

- 자기 자신을 다시 호출하는 함수
- 재귀함수 활용 시 종료 조건을 명시해주어야 함
    
    ```python
    def recursive_function(i) :
    		if (i == 10) :
    				return
    		print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출합니다")
    		recursive_function(i+1)
    ```
    

- ex) 팩토리얼 예제
    
    ```python
    def factorial(n) :
    		if (n <= 1) :
    				return 1
    		return n * factorial(n-1)
    ```
    

## DFS (깊이 우선 탐색)

- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 소요 시간 : `O(N)`
- 기존의 `인접행렬방식` :
    - 2차원 배열에 각 노드가 연결된 형태를 기록함
    - 연결이 되어있지 않는 노드(인접하지 않은 노드) = 무한의 비용으로 작성됨
        
        → 노드 간의 모든 관계를 기록하므로 불필요한 메모리가 낭비됨
        
- DFS :
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 진행
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 노드를 스택에 넣고 방문처리를 함
        
        방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
        
    3. 2를 더이상 수행하지 못할 때까지 반복함

- ex)
    
    ![2024-03-09_02-54-48.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/809ad7d1-1d8f-4d4f-b111-8a9ef10ef3f5/2024-03-09_02-54-48.jpg)
    
    에서 1부터 탐색을 진행하는 경우 :
    

![2024-03-09_02-56-45.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/ae952371-1fa0-4822-bc2d-686e20b6316a/2024-03-09_02-56-45.jpg)

![2024-03-09_02-57-08.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/272c00d3-f1f2-4c6f-a1f5-3559ef491d67/2024-03-09_02-57-08.jpg)

![2024-03-09_02-57-48.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/fd093862-d954-491c-a3e8-63a0cd1b4d5a/2024-03-09_02-57-48.jpg)

![2024-03-09_02-57-59.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/b8817141-93d7-4a1e-bc73-c8389b2dcb3a/2024-03-09_02-57-59.jpg)

: 1 → 2 → 7 → 6 → 8 → 3 → 4 → 5

- 재귀 함수를 활용해 구현하는 경우 :
    
    ```python
    def dfs(graph, v, visited) :
    		# 현재 노드 방문 처리
    		visited[v] = True
    		print(v, end='')
    		# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    		for i in graph[v] :
    				if not visited :
    						dfs(graph, i, visited)
    ```
    
    ```python
    graph = [
    		[],
    		[2,3,8],
    		[1,7],
    		[1,4,5],
    		[3,5],
    		[3,4],
    		[7],
    		[2,6,8],
    		[1,7]
    ]
    
    visited = [False] * 9
    ```
    

## BFS (너비 우선 탐색)

- 그래프에서 가까운 노드부터 탐색하는 알고리즘
- `Queue` 활용
- BFS :
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 진행
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입 후 방문 처리
    3. 2번 과정 더 이상 수행할 수 없을 때까지 반복

![2024-03-09_03-15-19.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/402dd4a0-8151-4078-b963-b1e492d1c3ca/2024-03-09_03-15-19.jpg)

![2024-03-09_03-16-05.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/de8ce62c-8ea9-4182-a238-ebfeca048271/2024-03-09_03-16-05.jpg)

![2024-03-09_03-15-30.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/6067dbb2-3ac6-40f3-935d-4ba9e23cef9c/2024-03-09_03-15-30.jpg)

- 재귀 함수 없이 queue 활용 :
    
    ```python
    from collections import deque
    
    def bfs(graph, start, visited) :
    		# 큐 설정
    		queue = deque([start])
    		# 현재 노드 방문 처리
    		visited[start] = True
    		# 큐가 빌 때까지 반복
    		while queue:
    				# 큐에서 하나의 원소를 뽑아 출력
    				v = queue.popleft()
    				print(v, end='')
    				for i in graph[v] :
    						if not visited[i] :
    								queue.append(i)
    								visited[i] = True	
    ```
    

## 1. 얼음틀 얼음 개수 구하기

<aside>
❔ N x M 크기의 얼음틀에 구멍이 뚫린 부분은 0, 채워진 부분은 1로 구분되어 있다.
(1 ≤ N,M ≤ 1000)

구멍이 뚫려있는 부분끼리 상하좌우로 붙어있는 경우 서로 연결되어 하나의 얼음이 생성된다.

얼음 틀의 모양이 주어졌을 때 생성되는 총 얼음의 개수를 구하시오.

</aside>

![2024-03-11_01-26-30.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/8ba2f755-32c8-4431-b401-eb7b32b7e151/2024-03-11_01-26-30.jpg)

- DFS 적용 방법
    - 0인 값이 연결되어 있는 노드끼리 묶어서 묶음 찾기
    1. 특정 지점의 상하좌우를 본 후 주변 지점 중 0이면서 아직 방문하지 않는 지점이 있다면 방문
    2. 방문 후 다시 상하좌우를 본 후 다시 진행해 모든 지점 방문 가능
    3. 1~2를 모든 노드에 반복해보며 방문하지 않은 지점의 수를 셈
    
    ⇒ 모든 노드 방문해보며 0인 경우 1로 바꾸며 이어진 끝을 찾아 모두 1로 바꾼 후 다른 0 탐색
    
    ```python
    # N, M 입력받기
    n, m = map(int, input().split())
    
    # 맵 정보 입력받기 
    iceMap = []
    for i in range(n) :
        iceMap.append(list(map(int, input())))
    
    # DFS로 특정 노드 방문 뒤에 연결된 모든 노드들에 방문
    def dfs(x, y) :
        # 범위에서 벗어나는 경우 즉시 종료
        if (x <= -1 or x >= n or y <= -1 or y >= n) :
            return False
        # 방문하지 않은 0인 경우, 방문 처리 후 상하좌우 재귀적 호출
        if (iceMap[x][y] == 0) :
            iceMap[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
        return False
    
    # 모든 노드에 대해 1로 만들기
    result = 0
    for i in range(n) :
        for j in range(m) :
            if (dfs(i,j) is True) :
                result += 1
    
    print(result)
    ```
    

## 2. 미로 탈출하기

<aside>
❔ N x M 크기의 미로에서 괴물을 피해 탈출해야 한다.
(14≤ N,M ≤ 200)

시작점은 (1,1), 출구는 (N,M)이며, 괴물이 있는 부분은 0, 없는 길은 1로 표시된다.

미로를 탈출하기 위한 최소 칸의 개수를 구하시오.

</aside>

![2024-03-11_02-04-59.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/6fd785d8-140c-43d0-ba33-3acdb752c9d8/2024-03-11_02-04-59.jpg)

- BFS 활용 풀이
    - BFS : 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하게 됨
    - 시작점부터, 다음 노드에 방문 시 시작점에서부터의 거리를 +1해서 리스트에 저장함
    - 예시:
        
        ![2024-03-11_02-07-10.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/6ee82ae0-95cc-4aae-a812-1c9c854f3d2e/2024-03-11_02-07-10.jpg)
        
    
    ```python
    from collections import deque
    
    # N, M 입력받기
    n, m = map(int, input().split())
    
    # 미로 맵 정보 입력받기
    maze = []
    for i in range(n) :
        maze.append(list(map(int, input())))
    
    # 상하좌우 방향 정의
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    # BFS 구현
    def bfs(x, y):
        queue = deque()
        queue.append((x,y))
        # 큐가 모두 빌 때까지 반복
        while queue :
            x, y = queue.popleft()
            # 현재 위치에서 상하좌우 확인
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx < 0 or nx >= n or ny < 0 or ny >= m) :
                    continue
                if (maze[nx][ny] == 0) :
                    continue
                # 조건을 만족하는 해당 노드를 처음 방문하는 경우 최단 거리로 기록
                if (maze[nx][ny] == 1) :
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
        return maze[n-1][m-1]
    
    print(bfs(0,0))
    ```