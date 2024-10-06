'''
<13549. 숨바꼭질3>
골드5
https://www.acmicpc.net/problem/13549
'''

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동

from collections import deque

# 수빈 위치 N, 동생 위치 K
n, k = map(int, input().split())

# 시간 테이블 생성
d = [100000] * 100001
d[n] = 0

# bfs 진행
q = deque()
q.append(n)
while q:
    i = q.popleft()
    if i < 50001:
        if d[2*i] > d[i] + 1:
            d[2*i] = d[i]
            q.append(2*i)
    if i > 0:
        if d[i-1] > d[i] + 1:
            d[i-1] = d[i] + 1
            q.append(i-1)
    if i < 100000:
        if d[i+1] > d[i] + 1:
            d[i+1] = d[i] + 1
            q.append(i+1)
    
print(d[k])