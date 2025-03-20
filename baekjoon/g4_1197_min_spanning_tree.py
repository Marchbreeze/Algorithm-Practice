'''
<1197. 최소 스패닝 트리>
골드4
https://www.acmicpc.net/problem/1197
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 노드 개수, 간선(union) 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블에 자기 자신으로 초기화하기
parent = [i for i in range(v+1)]

# 모든 간선 정보 입력받고 비용 순으로 정렬하기
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x: x[2])

def find_parent(x):
    if (parent[x] != x):
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if (a < b):
        parent[b] = find_parent(a)
    else:
        parent[a] = find_parent(b)

# 간선 하나씩 확인하기
total = 0
for edge in edges:
    a, b, cost = edge
    # 사이클이 발생하지 않으면 집합 포함
    if (find_parent(a) != find_parent(b)):
        union_parent(a, b)
        total += cost

print(total)