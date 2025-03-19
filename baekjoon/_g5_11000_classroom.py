'''
<11000. 강의실 배정>
골드5
https://www.acmicpc.net/problem/11000
'''

# note : 해당 시간에 동시 진행중인 강의 개수를 계속 저장하지 않고, 시작점 & 끝점만 기록한 뒤 0부터 계속 시작(+),끝(-)하면서 최대 지점 확인하는 방법
# = Sweep Line 알고리즘

from collections import defaultdict

n = int(input())
diff = defaultdict(int)

for _ in range(n):
    start, end = map(int, input().split())
    diff[start] += 1   # 구간 시작시 +1
    diff[end] -= 1     # 구간 종료시 -1

current = 0
max_overlap = 0
for point in sorted(diff):
    current += diff[point]
    max_overlap = max(max_overlap, current)

print(max_overlap)