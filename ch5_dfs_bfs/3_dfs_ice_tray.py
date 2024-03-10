
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