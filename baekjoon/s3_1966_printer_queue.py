'''
<1966. 프린터 큐>
실버3
https://www.acmicpc.net/problem/1966
'''

from collections import deque
import heapq

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    q = deque(array)
    h = [-i for i in array]
    count = 0
    while True:
        aim = heapq.heappop(h) * -1
        poped = q.popleft()
        while aim != poped:
            q.append(poped)
            poped = q.popleft()
        count += 1
        if poped == m:
            print(count)
            break
