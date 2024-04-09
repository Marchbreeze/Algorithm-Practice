'''
<2164. 카드2>
실버4
https://www.acmicpc.net/problem/2164
'''

# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있음
# 제일 위에 있는 카드를 버리고 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기는 과정을 한장 남을때까지 반복

# 리스트의 pop은 O(N)의 시간 복잡도를 가지고 있기에 deque를 사용해야함 !!!!
from collections import deque

# 정수 입력
n = int(input())

# 리스트 생성
array = deque()

for i in range(1,n+1) :
    array.append(i)

# 과정 반복
for i in range(n-1):
    array.popleft()
    array.append(array.popleft())

print(array[0])