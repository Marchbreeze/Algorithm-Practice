'''
<21609. 상어 중학교>
골드5
https://www.acmicpc.net/problem/21609
'''

# 게임은 크기가 N×N인 격자에서 진행되고, 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록
# 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현
# 검은색 블록은 -1, 무지개 블록은 0으로 표현

# 블록 그룹은 연결된 블록의 집합
# 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록

# 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복
# 1. 크기가 가장 큰 블록 그룹을 찾는다.
#    그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
#    그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
#    그 것도 여러개이면 열이 가장 큰 것을 찾는다.
# 2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
# 3. 격자에 중력이 작용한다.
#    격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
# 4. 격자가 90도 반시계 방향으로 회전한다.
# 5. 다시 격자에 중력이 작용한다.

from collections import deque

# 격자 한 변의 크기 N, 색상의 개수 M (1 ≤ N ≤ 20, 1 ≤ M ≤ 5)
n, m = map(int, input().split())

# N개의 줄에 격자의 칸에 들어있는 블록의 정보
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 방향 설정
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > n-1

# BFS로 가장 큰 영역 찾기
result = 0
is_finished = False
def delete_largest_group_by_bfs():
    visited = [[False] * n for _ in range(n)]
    blocks = []
    q = deque()
    for y in range(n):
        for x in range(m):
            # 일반 블록일때만 탐색
            if board[y][x] in [0,-1,-2] or visited[y][x] is True:
                continue
            q.append((y,x))
            color = board[y][x]
            block = [[],0,0,0,0,0,[]] # 0: yx 좌표 리스트, 1: 최대값, 2: 기준블록 y, 3: 기준블록 x, 4: 무지개 개수, 5:전체 개수, 6:무지개 좌표 리스트
            while q:
                sy, sx = q.popleft()
                for i in range(4):
                    ny = sy + dy[i]
                    nx = sx + dx[i]
                    if out_of_range(ny,nx) or visited[ny][nx] is True or board[ny][nx] not in [color, 0] :
                        continue
                    if board[ny][nx] == 0:
                        block[4] += 1
                        block[6].append((ny,nx))
                    else:
                        block[1] = max(block[1], board[ny][nx])
                        block[2] = max(block[2], ny)
                        block[3] = max(block[3], x)
                    visited[ny][nx] = True
                    block[0].append((ny,nx))
                    q.append((ny,nx))
                    block[5] += 1
            # 무지개 블록 방문 초기화
            for j in range(block[4]):
                visited[block[6][j][0]][block[6][j][1]] = False
            # 블록 정보 저장
            blocks.append(block)

    # 조건 만족하는 블록 찾기
    blocks.sort(key=lambda x: (-x[5], x[2], x[3]))

    global is_finished
    global result
    # 블록 크기가 2보다 작으면 정지
    if len(blocks) == 0:
        is_finished = True
    elif blocks[0][5] < 2:
        is_finished = True
    else:
        # 블록 지우고 점수 계산하기
        for i in range(blocks[0][5]):
            board[blocks[0][0][i][0]][blocks[0][0][i][1]] = -2
        result += blocks[0][5] ** 2

# 중력 작용 (빈칸 -2, 고정블록 -1)
# 세로줄마다 아래부터 확인, 빈칸 있으면 고정 or 벽 전까지 모두 내리기
def force_gravity():
    for x in range(n):
        for y in range(n-1,-1,-1):
            for i in range(n-1,0,-1):
                if board[i][x] == -2 and board[i-1][x] != -1:
                    board[i][x], board[i-1][x] = board[i-1][x], board[i][x]

# 90도 반시계방향 돌리기
def turn_table():
    global board
    temp_table = [[] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            temp_table[y].append(board[n-1-x][y])
    board = temp_table

# 반복 진행
while True:
    for i in range(n):
        print(' '.join(map(str, board[i])))
    delete_largest_group_by_bfs()
    if is_finished:
        print(result)
        break
    force_gravity()
    turn_table()
    force_gravity()