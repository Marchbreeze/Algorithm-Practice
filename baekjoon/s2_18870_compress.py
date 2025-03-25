'''
<18870. 좌표 압축>
실버2
https://www.acmicpc.net/problem/18870
'''
from collections import defaultdict

n = int(input())
array = list(map(int, input().split()))

d = defaultdict(int)
for num in array:
    d[num] += 1

order = defaultdict(int)
keys = sorted(d.keys())
for i in range(len(keys)):
    order[keys[i]] = i

print(" ".join(str(order[i]) for i in array))