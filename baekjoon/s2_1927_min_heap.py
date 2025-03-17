'''
<1927. 최소 힙>
실버2
https://www.acmicpc.net/problem/1927
'''

import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if (x == 0):
        if (len(hq) == 0):
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)
