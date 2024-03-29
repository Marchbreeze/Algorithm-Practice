
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


# N, M 입력받기
n, m = map(int, input().split())

# 부모 테이블 0으로 설정하기
parent = [0] * (n+1)

# 부모 테이블에 자기 자신으로 초기화하기
for i in range(1, n+1):
    parent[i] = 1
		
# 연산 입력받고 해당 연산 수행하기
for i in range(m):
    oper, a, b = map(int, input().split())
    if (oper == 0):
        union_parent(parent,a,b)
    elif (oper == 1):
        if (find_parent(parent,a) == find_parent(parent,b)):
            print("YES")
        else:
            print("NO")