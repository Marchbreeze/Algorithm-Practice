'''
<15659. 연산자 끼워넣기 (3)>
골드4
https://www.acmicpc.net/problem/15659
'''

from collections import deque

# 수 개수
n = int(input())

# 수 리스트
nums = list(map(int, input().split()))

# +, -, *, // 개수
op = list(map(int, input().split()))

# 수식 모ㅁ
result = []

q = deque()
q.append((str(nums[0]),0,op[0],op[1],op[2],op[3]))
while q:
    sentence, count, pl, mi, ti, di = q.popleft()
    if count == 2*n-2:
        result.append(sentence)
    else:
        count += 1
        if (count % 2 == 0):
            q.append((sentence+str(nums[count//2]), count, pl, mi, ti, di))
        else:
            if pl != 0:
                q.append((sentence+"+", count, pl-1, mi, ti, di))
            if mi != 0:
                q.append((sentence+"-", count, pl, mi-1, ti, di))
            if ti != 0:
                q.append((sentence+"*", count, pl, mi, ti-1, di))
            if di != 0:
                q.append((sentence+"//", count, pl, mi, ti, di-1))

_list = []
for sentence in result:
    _list.append(eval(sentence))
print(max(_list))
print(min(_list))