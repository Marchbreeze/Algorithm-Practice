'''
<9375. 패션왕 신해빈>
실버3
https://www.acmicpc.net/problem/9375
'''
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(set)

    for _ in range(n):
        name, item = map(str, input().split())
        d[item].add(name)

    count = 1
    for key in d.keys():
        count *= len(d[key]) + 1
    print(count - 1)