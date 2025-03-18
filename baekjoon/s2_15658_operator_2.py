'''
<15658. 연산자 끼워넣기>
실버2
https://www.acmicpc.net/problem/15658
'''

# N개의 수로 이루어진 수열 (순서 조정 X)
# N-1개의 연산자 +, -, *, //
# 연산자 우선 순위를 무시 & 나눗셈은 몫만 취함 & 음수 나눗셈은 양수로 바꾼뒤 수행 후 다시 변환 -> 식의 최대 최소 구하기

from collections import deque

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