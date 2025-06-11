
# 특정 원소 속한 집합 찾기
def find_parent(parent, x):
	if (parent[x] != x) :
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

# 두 원소 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else :
        parent[a] = b

# 노드 개수, 간선(union) 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 0으로 설정하기
parent = [0] * (v+1)

# 부모 테이블에 자기 자신으로 초기화하기
for i in range(1, v+1):
    parent[i] = 1

# 간선, 최종 비용 담을 변수 설정하기
edges = []
result = 0

# 모든 간선 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

# 간선 비용순으로 정렬하기
edges.sort()

# 최소 신장 트리 중 가장 비용이 큰 간선
last = 0

# 간선 하나씩 확인하기
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않으면 집합 포함
    if (find_parent(parent, a) != find_parent(parent, b)):
        union_parent(parent, a, b)
        result += cost
        last = cost

# 가장 비용이 큰 간선 제외 비용
print(result - cost)