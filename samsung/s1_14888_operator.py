'''
<14888. 연산자 끼워넣기>
실버1
https://www.acmicpc.net/problem/14888
'''

# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
# 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성

from collections import deque

'''
[노트]
첫 숫자에서 마지막 노드까지 존재하는 연산자로 모두 시도 (4방향 가는 것처럼)
큐 안에는 (진행중인 연산 결과, 숫자 번쨰, 연산자개수)
'''

# 수 개수
n = int(input())

# 수 리스트
nums = list(map(int, input().split()))

# +, -, *, // 개수
op = list(map(int, input().split()))

# 최대 최소
result = []

q = deque()
q.append((nums[0],0,op[0],op[1],op[2],op[3]))
while q:
    num, count, pl, mi, ti, di = q.popleft()
    if count == n-1:
        result.append(num)
    else:
        count += 1
        if pl != 0:
            q.append((num+nums[count], count, pl-1, mi, ti, di))
        if mi != 0:
            q.append((num-nums[count], count, pl, mi-1, ti, di))
        if ti != 0:
            q.append((num*nums[count], count, pl, mi, ti-1, di))
        if di != 0:
            q.append((int(num/nums[count]), count, pl, mi, ti, di-1))

print(max(result))
print(min(result))