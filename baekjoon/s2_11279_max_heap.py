'''
<11279. 최대 힙>
실버2
https://www.acmicpc.net/problem/11279
'''

import heapq
import sys

input = sys.stdin.readline

n = int(input())
array = []
h = heapq.heapify(array)

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(array) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(array))
    else:
        heapq.heappush(array, x * -1)