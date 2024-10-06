'''
<13913. 숨바꼭질4>
골드4
https://www.acmicpc.net/problem/13913
'''

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

from collections import deque

'''
시도:
- 동선 테이블 생성 : r = [[n] for _ in range(100001)]
-> 메모리 초과 !
배열에 카운트와 직전 위치 정보를 저장하면 쉽게 해결
'''

# 수빈 위치 N, 동생 위치 K
n, k = map(int, input().split())

# 시간 테이블 생성
d = [[100000, -1] for _ in range(100001)]
d[n] = [0,-1]

# bfs 진행
q = deque()
q.append(n)
while q:
    i = q.popleft()
    if i == k:
        break
    if i < 50001:
        if d[2*i][0] > d[i][0] + 1:
            d[2*i][0] = d[i][0] + 1
            d[2*i][1] = i
            q.append(2*i)
    if i > 0:
        if d[i-1][0] > d[i][0] + 1:
            d[i-1][0] = d[i][0] + 1
            d[i-1][1] = i
            q.append(i-1)
    if i < 100000:
        if d[i+1][0] > d[i][0] + 1:
            d[i+1][0] = d[i][0] + 1
            d[i+1][1] = i
            q.append(i+1)

# 경로 뒤로 쫒기    
route = [k]
for i in range(d[k][0]):
    route.insert(0, d[route[0]][1])

print(d[k][0])
print(' '.join(map(str, route)))