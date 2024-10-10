'''
<9663. N-Queen>
골드4
https://www.acmicpc.net/problem/9663
'''

# 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제 (N:1~15)
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성

'''
nxn에 n개 -> 가로, 세로 인덱스가 모두 달라야함
대각선 방지 (x, y축 차이가 같으면 안됨)
'''

# 크기 입력
n = int(input())

# 리스트의 각 칸 : x값, 각 칸의 수: y값
count = 0

# 백트래킹 진행
stack = [[]]
while stack:
    saved = stack.pop()
    m = len(saved)
    # 길이 채워지면 마감
    if m == n:
        count += 1
        continue
    # 새로 추가할 수
    for i in range(n):
        # 존재여부 비교
        if i not in saved:
            # 기존 stack의 저장값
            for j in range(m):
                # 대각선 비교 (추가되면 (m+1,i) 좌표)
                if abs(m-j) == abs(saved[j]-i):
                    break
            else:
                stack.append(saved + [i])

print(count)