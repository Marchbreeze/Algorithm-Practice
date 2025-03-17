'''
<5430. AC>
골드5
https://www.acmicpc.net/problem/5430

[놓친 부분]
연산 과정에서 deque를 계속 reverse를 해주면, O(N)의 시간 복잡도 발생
100,000 크기의 n과 p에서 RRR...이 나오게 되면 결국 O(N2)의 시간 복잡도 발생 가능
direction 변수로 뒤집는 상황임을 기록하고, 마지막 결과 처리 때에 한번만 진행
'''

from collections import deque

t = int(input())
for _ in range(t):
    methods = list(input())
    n = int(input())
    nums = []
    nums_input = input()
    if (n != 0):
        nums = list(nums_input[1:-1].split(','))
    direction = 1

    dq = deque(nums)
    for m in methods:
        if (m == "R"):
            direction *= -1
        elif (len(dq) == 0):
            print("error")
            break
        else:
            if (direction == 1):
                dq.popleft()
            else:
                dq.pop()
    else:
        if (direction == 1):
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")
            