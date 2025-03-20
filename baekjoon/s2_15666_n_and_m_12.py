'''
<15666. N과 M(12)>
실버2
https://www.acmicpc.net/problem/15666
'''
from collections import deque

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

q = deque()
q.append(([], 0, 0))

while q:
    saved, prev, count = q.popleft()
    if count == m:
        print(' '.join(map(str, saved)))
    else:
        for num in nums:
            if (num >= prev):
                q.append((saved + [num], num, count + 1))