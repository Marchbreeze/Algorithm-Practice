'''
<2531. 회전초밥>
실버1
https://www.acmicpc.net/problem/2531
'''
from collections import deque

# 접시수, 초밥종류수, 연속수, 쿠폰접시
n, d, k, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array += array[:k-1]

q = deque(array[:k])
result = len(set(list(q) + [c]))

for j in range(k, n+k-1):
    q.append(array[j])
    q.popleft()
    result = max(result, len(set(list(q) + [c])))

print(result)