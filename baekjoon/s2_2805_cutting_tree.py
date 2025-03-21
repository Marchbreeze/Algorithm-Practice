'''
<2805. 나무 자르기>
실버2
https://www.acmicpc.net/problem/2805
'''

n, m = map(int, input().split())
heights = list(map(int, input().split()))

h = 0
start, end = 0, max(heights)

while True:
    if (start > end):
        break
    mid = (start + end) // 2
    count = 0
    for tree in heights:
        if (tree > mid):
            count += tree - mid
    if (count >= m):
        h = mid
        start = mid + 1
    else:
        end = mid - 1

print(h)
