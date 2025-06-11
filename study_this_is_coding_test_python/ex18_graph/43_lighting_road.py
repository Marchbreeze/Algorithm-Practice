'''
< 43. 어두운 길 > - 크루스칼 예제
마을에 N개의 집(0~N-1번)과 M개의 도로가 있다.
모든 도로에는 가로등이 있고, 켜기 위한 비용이 존재한다.
일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 어갈 수 있도록 한다.
일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 구하시오.
(1 <= N < M <= 200,000)
'''

# 집, 도로 개수 입력
n, m = map(int, input().split())

# 도로 정보 입력
roads = []
for i in range(m):
    x, y, cost = map(int, input().split())
    roads.append((cost, x, y))
roads.sort()

# 두 원소 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else :
        parent[a] = b

# 특정 원소 속한 집합 찾기
def find_parent(parent, x):
    if (parent[x] != x) :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 부모 테이블 설정
parent = [0] * n

for i in range(n):
    parent[i] = i

# 간선 하나씩 확인
result = 0
total = 0
for road in roads:
    cost, a, b = road
    total += cost
    if (find_parent(parent, a) != find_parent(parent, b)):
        union_parent(parent, a, b)
        result += cost

print(total - result)