'''
<1806. 부분합>
골드4
https://www.acmicpc.net/problem/1806
'''
import sys

n, s = map(int, input().split())
array = list(map(int, input().split()))

left, right = 0, 0
interval_count = 0
interval_sum = 0
min_length = sys.maxsize

while True:
    if interval_sum >= s:
        min_length = min(min_length, right - left)
        interval_sum -= array[left]
        left += 1
    elif right == n:
        break
    else:
        interval_sum += array[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)