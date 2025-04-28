'''
<1920. 수 찾기>
실버4
https://www.acmicpc.net/problem/1920
'''
from collections import defaultdict

n = int(input())
array_n = list(map(int, input().split()))
m = int(input())
array_m = list(map(int, input().split()))

d = defaultdict(int)

for num_n in array_n:
    d[num_n] += 1

for num_m in array_m:
    if d[num_m] == 0:
        print(0)
    else:
        print(1)