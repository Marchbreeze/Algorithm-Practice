'''
<12851. 숨바꼭질2>
골드4
https://www.acmicpc.net/problem/12851
'''

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성

from collections import deque

# 수빈 위치 N, 동생 위치 K
n, k = map(int, input().split())

# 시간 테이블 생성
d = [100000] * 100001
d[n] = 0

# 방법 테이블 생성
c = [0] * 100001
c[n] = 1

# bfs 진행
q = deque()
q.append(n)
while q:
    i = q.popleft()
    if i < 50001:
        if d[2*i] > d[i] + 1:
            d[2*i] = d[i] + 1
            c[2*i] = c[i]
            q.append(2*i)
        elif d[2*i] == d[i] + 1:
            c[2*i] += c[i]
    if i < 100000:
        if d[i+1] > d[i] + 1:
            d[i+1] = d[i] + 1
            c[i+1] = c[i]
            q.append(i+1)
        elif d[i+1] == d[i] + 1:
            c[i+1] += c[i]
    if i > 0:
        if d[i-1] > d[i] + 1:
            d[i-1] = d[i] + 1
            c[i-1] = c[i]
            q.append(i-1)
        elif d[i-1] == d[i] + 1:
            c[i-1] += c[i]
    
print(d[k])
print(c[k])