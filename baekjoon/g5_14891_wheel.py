'''
<14891. 톱니바퀴>
골드5
https://www.acmicpc.net/problem/14891
'''

from collections import deque

'''
큐의 rotate 활용
'''

# 각 바퀴별 톱니 설정
q = [deque(), deque(), deque(), deque()]
for i in range(4):
    q[i].extend(map(int, input()))

# 회전 설정
k = int(input())
spins = []
for _ in range(k):
    spins.append(list(map(int, input().split())))

for spin in spins:
    i, d = spin
    i -= 1
    # 인접 바퀴 확인
    need_spin = [0] * 4
    need_spin[i] = d
    for j in range(1,4):
        if i+j <= 3 and q[i+j][6] != q[i+j-1][2]:
            need_spin[i+j] = d*(-1)**j
        else:
            break
    for j in range(1,4):
        if i-j >= 0 and q[i-j][2] != q[i-j+1][6]:
            need_spin[i-j] = d*(-1)**j
        else:
            break
    # 회전
    for j in range(4):
        q[j].rotate(need_spin[j])

print(q[0][0] + q[1][0]*2 + q[2][0]*4 + q[3][0]*8)