'''
<10974. 모든 순열>
실버3
https://www.acmicpc.net/problem/10974
'''

import itertools

n = int(input())
_list = list(itertools.permutations([i for i in range(1, n+1)], n))
for p in _list:
    print(" ".join(map(str, p)))