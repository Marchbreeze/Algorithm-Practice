'''
<14235. 크리스마스 선물>
실버3
https://www.acmicpc.net/problem/14235
'''

import heapq

n = int(input())
q = []

for _ in range(n):
    a = list(map(int, input().split()))
    if (a[0] == 0):
        if (len(q) != 0):
            print(-1 * heapq.heappop(q))   
        else:
            print(-1)
    else:
        for item in a[1:]:
            heapq.heappush(q, -1 * item)