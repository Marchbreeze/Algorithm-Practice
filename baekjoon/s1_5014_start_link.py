'''
<5014. 스타트링크>
실버1
https://www.acmicpc.net/problem/5014
'''

# 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동
# 엘리베이터는 버튼이 2개밖에 없다. U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼
# G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성
# 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력

from collections import deque

# 숫자 입력
f, s, g, u, d = map(int, input().split())

# 층별 도달시간 배열 생성
arr = [-1] * (f+1)
arr[s] = 0

# bfs 진행
q = deque()
q.append(s)
while q:
    i = q.popleft()
    if i <= f-u and (arr[i+u] == -1 or arr[i+u] > arr[i] + 1):
        arr[i+u] = arr[i] + 1
        q.append(i+u)
    if i > d and (arr[i-d] == -1 or arr[i-d] > arr[i] + 1):
        arr[i-d] = arr[i] + 1
        q.append(i-d)

if arr[g] != -1:
    print(arr[g])
else:
    print("use the stairs")
