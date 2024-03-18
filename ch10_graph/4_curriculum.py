
from collections import deque
import copy

# 노드 개수 입력받기
v = input().split()

# 0으로 초기화된 진입차수 리스트 설정하기
indegree = [0] * (v+1)

# 0으로 초기화된 강의시간 리스트 설정하기
time = [0] * (v+1)

# 간선 정보 담을 2차원 리스트 설정하기
graph = [[] for i in range(v+1)]

# 모든 간선 정보 입력받기 & 진입차수 기록하기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1] :
        indegree[i] += 1
        graph[x].append(i)
		
# 위상 정렬
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if (indegree[i] == 0):
            q.append(i) 
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 뺴내기
        now = q.popleft()
        # 연결된 노드의 진입차수 뺴기
        for i in graph[now]:
            result = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            # 진입차수가 0이 되면 큐에 넣기
            if (indegree[i] == 0):
                q.append(i) 

    # 결과 출력
    for i in range(1, v+1):
            print(result[i])

topology_sort()