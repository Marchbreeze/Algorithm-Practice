'''
<21736. 헌내기는 친구가 필요해>
실버2
https://www.acmicpc.net/problem/21736
'''
from collections import deque

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]
print(array)

dy = [0,0,-1,1]
dx = [1,-1,0,0]

q = deque()
count = 0

# 도연이 찾기
for i in range(n):
    for j in range(m):
        if array[i][j] == "I":
            q.append((i,j))
            array[i][j] == "X"
            break

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or ny>n-1 or nx<0 or nx>m-1:
            continue
        new = array[ny][nx]
        if new == "X":
            continue
        if new == "P":
            count += 1
        array[ny][nx] = "X"
        q.append((ny, nx))
    
if count == 0:
    print("TT")
else:
    print(count)