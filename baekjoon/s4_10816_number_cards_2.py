'''
<10816. 숫자 카드 2>
실버4
https://www.acmicpc.net/problem/10816
'''
from collections import defaultdict

n = int(input())
array_n = list(map(int, input().split()))
m = int(input())
array_m = list(map(int, input().split()))

answer = []

d = defaultdict(int)
for num_n in array_n:
    d[num_n] += 1
for num_m in array_m:
    answer.append(d[num_m])

print(' '.join(map(str, answer)))