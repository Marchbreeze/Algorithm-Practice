'''
<13335. 트럭>
실버1
https://www.acmicpc.net/problem/13335
'''

# 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n 개의 트럭이 건너가려고 한다. 
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.
# 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다.
# 다리의 길이는 w 단위길이(unit distance)이며, 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.
# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때, 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성

from collections import deque

''' 
[노트]
일단 첫번쨰 트럭 출발 (1초, 큐 00..07)
다음 초에 앞에 0 빼고, 뒤에 넣을 수 있는지 무게 확인 후 넣기
큐가 모두 0이 되면 종료
'''

# 트럭 개수 n, 최대 트럭개수 w, 최대 트럭하중 t
n, w, t = map(int, input().split())

# 각 트럭별 무게
weight = deque(list(map(int, input().split())))

# 다리 위 트럭 리스트 추가
q = deque()
for _ in range(w):
    q.append(0)
second = 0

# 트럭 모두 보낼때까지 반복
while True:
    second += 1
    q.popleft()
    if sum(weight) != 0:
        if sum(q) + weight[0] > t or sum(weight) == 0:
            q.append(0)
        else:
            q.append(weight.popleft())
    if sum(q) == 0:
        break

print(second)
