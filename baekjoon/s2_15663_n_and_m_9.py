'''
<15663. N과 M(9)>
실버2
https://www.acmicpc.net/problem/15663
'''
from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

q = deque()
q.append([0, [], []])
result = set()

while q:
    count, indexs, saved = q.popleft()
    if count == m:
        result.add(tuple(saved))
    else:
        for i in range(n):
            if i not in indexs:
                q.append([count+1, indexs + [i], saved + [nums[i]]])

result = sorted(list(result))
for p in result:
    print(' '.join(map(str, p)))