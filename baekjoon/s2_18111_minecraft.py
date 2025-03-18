'''
<18111. 마인크래프트>
실버2
https://www.acmicpc.net/problem/18111
'''

# 세로 N, 가로 M 크기의 집터, 집터 맨 왼쪽 위의 좌표는 (0, 0) & 인벤토리에는 B개의 블록이 들어 있음
# 작업 1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. (2초 소요)
# 작업 2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. (1초 소요)
# 집터 내의 땅의 높이를 일정하게 바꾸는 최소 시간과 땅 높이 도출

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
_list = []
for _ in range(n):
    _list += list(map(int, input().split()))
_list.sort()

min_time = int(1e9)
max_height = 0

max_block = _list[0]
min_block = _list[-1]

for height in range(max_block, min_block+1):
    time = 0
    inven_use = 0
    for j in range(m*n):
        h = height - _list[j]
        if (h > 0):
            time += h
            inven_use += h
        else:
            time += (-2) * h
            inven_use += h
    if (b >= inven_use and time <= min_time):
        min_time = time
        max_height = max(height, max_height)

print(min_time, max_height)