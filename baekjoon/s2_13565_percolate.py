'''
<13565. 침투>
실버2
https://www.acmicpc.net/problem/13565
'''

# 격자 크기 m, n
m, n = map(int, input().split())

# 격자 전류 통과 유무 (0이 가능)
arr = []
for _ in range(m):
    arr.append(list(map(int, input())))

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > m-1

def dfs(v) -> bool:
    stack = [(0,v)]
    visited = [[False] * n for _ in range(m)]

    while stack:
        y, x = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        if y == m-1:
            return True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if out_of_range(ny,nx) or arr[ny][nx] == 1 or visited[ny][nx] is True:
                continue
            stack.append((ny,nx))
    else:
        return False

# 첫줄 모두 체크
for i in range(n):
    if arr[0][i] == 1:
        continue
    if dfs(i):
        print("YES")
        break
else:
    print("NO")
    