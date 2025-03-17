'''
<4358. 생태학>
실버2
https://www.acmicpc.net/problem/4358
'''
from collections import defaultdict

d = defaultdict(int)
count = 0

while True:
    try:
        tree = input()
        d[tree] += 1
        count += 1
    except EOFError:
        break

for tree, num in sorted(d.items()):
    ratio = num / count * 100
    print(f'{tree} {ratio:.4f}')