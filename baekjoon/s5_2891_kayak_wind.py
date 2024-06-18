'''
<2891. 카약과 강풍>
실버5
https://www.acmicpc.net/problem/2891
'''

from collections import Counter

# 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R
n, s, r = map(int, input().split())

# 팀 저장 리스트
array = [0] * n

# 손상 -1
for i in list(map(int, input().split())):
    array[i-1] -= 1

# 여분 +1
for i in list(map(int, input().split())):
    array[i-1] += 1

# array 채우기
for i in range(n):
    if (array[i] == -1):
        if (i > 0):
            if (array[i-1] == 1):
                array[i], array[i-1] = 0, 0
        if (i < n-1):
            if (array[i+1] == 1):
                array[i], array[i+1] = 0, 0

# -1 개수 세기
count = Counter(array)
print(count[-1])