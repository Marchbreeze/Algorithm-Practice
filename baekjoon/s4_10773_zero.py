'''
<10773. 제로>
실버4
https://www.acmicpc.net/problem/10773
'''

from collections import deque

k = int(input())
dq = deque()

for _ in range(k):
    n = int(input())
    if (n == 0):
        dq.pop()
    else:
        dq.append(n)

print(sum(dq))