'''
<2075. N번째 큰 수>
실버3
https://www.acmicpc.net/problem/2075
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
_list = []
for _ in range(n):
    row = list(map(int, input().split()))
    for num in row:
        heapq.heappush(_list, num)
        if (len(_list) > n):
            heapq.heappop(_list)

print(heapq.nlargest(n, _list)[n-1])