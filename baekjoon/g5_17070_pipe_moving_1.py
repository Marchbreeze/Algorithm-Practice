'''
<17070. 파이프 옮기기 1>
골드5
https://www.acmicpc.net/problem/17070
'''

# 다음에 풀때는 dp로 풀어보기!

from collections import deque

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

# 0 가로 1 대각선 2 세로
q = deque()
q.append((0,1,0))

count = 0
while q:
    y, x, dir = q.popleft()
    if (y == n-1 and x == n-1) :
        count += 1
        continue
    if (x+1<n and array[y][x+1] != 1 and dir != 2):
        q.append((y, x+1, 0))
    if (y+1<n and array[y+1][x] != 1 and dir != 0):
        q.append((y+1, x, 2))
    if (x+1<n and array[y][x+1] != 1 and y+1<n and array[y+1][x] != 1 and array[y+1][x+1] != 1):
        q.append((y+1, x+1, 1))

print(count)