'''
<10026. 적록색약>
골드5
https://www.acmicpc.net/problem/10026
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
box = [input().rstrip() for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def out_of_bound(x,y):
    return x<0 or x>n-1 or y<0 or y>n-1

def is_next_unavailable(x,y,i):
    color = ['R', 'G', 'B', 'RB']
    if i == 3:
        return out_of_bound(x, y) or box[y][x] == 'B' or visited[y][x] is True
    else:
        return out_of_bound(x, y) or box[y][x] != color[i] or visited[y][x] is True

# R,G,B,RG 개수 확인
count = [0, 0, 0, 0]
for i in range(4):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for y in range(n):
        for x in range(n):
            if is_next_unavailable(x,y,i) is False:
                count[i] += 1
                q.append((x,y))
                visited[y][x] = True
                while q:
                    xx, yy = q.popleft()
                    for j in range(4):
                        nx = xx + dx[j]
                        ny = yy + dy[j]
                        if is_next_unavailable(nx,ny,i) is True:
                            continue
                        q.append((nx, ny))
                        visited[ny][nx] = True

not_blind = sum(count[0:3])
blind = sum(count[2:])
print(not_blind, blind)