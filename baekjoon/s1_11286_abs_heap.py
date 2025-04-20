'''
<11286. 절댓값 힙>
실버1
https://www.acmicpc.net/problem/11286
'''

import heapq

n = int(input())
hq_plus = []
hq_minus = []

for _ in range(n):
    x = int(input())
    if x != 0:
        if x>0:
            heapq.heappush(hq_plus, x)
        else:
            heapq.heappush(hq_minus, x * -1)
    else:
        pl = int(1e9)
        mi = int(1e9)
        if (len(hq_minus) != 0):
            mi = heapq.heappop(hq_minus) # 절댓값 음수
        if (len(hq_plus) != 0):
            pl = heapq.heappop(hq_plus)
        if (mi == int(1e9) and pl == int(1e9)):
            print(0)
        else:
            if (mi <= pl):
                print(mi * -1)
                heapq.heappush(hq_plus, pl)
            else:
                print(pl)
                heapq.heappush(hq_minus, mi)