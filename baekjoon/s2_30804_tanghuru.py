'''
<30804. 과일 탕후루>
실버2
https://www.acmicpc.net/problem/30804
'''
from collections import defaultdict
from collections import deque

n = int(input())
array = list(map(int, input().split()))
d = defaultdict(int)
dq = deque()
result = 1
index = 0

while True:
    notNullCount = [x for x in d.values() if x > 0]
    if len(notNullCount) <= 2:
        result = max(result, sum(d.values()))
        if index == n:
            break
        dq.append(array[index])
        d[array[index]] += 1
        index += 1
    else:
        last = dq.popleft()
        d[last] -= 1

print(result)