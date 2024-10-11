'''
<3190. 뱀>
골드4
https://www.acmicpc.net/problem/3190
'''

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1, 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산

from collections import deque

# 보드의 크기 N (2 ≤ N ≤ 100)
N = int(input())

# 사과의 개수 K (0 ≤ K ≤ 100)
K = int(input())

# 사과의 위치
apple = []
for _ in range(K):
    y, x = map(int, input().split())
    apple.append((y-1,x-1))

# 방향 변환 횟수 L (1 ≤ L ≤ 100)
L = int(input())

# 방향 변환 정보
moves = []
for _ in range(L):
    dist, dir = input().split()
    moves.append((int(dist), dir))

dy = [0,1,0,-1]
dx = [1,0,-1,0]

# 큐로 뱀 위치 관리
snake = deque()
y, x = 0, 0
snake.append((y,x))

count = 0
d = 100
isFinished = False
for i in range(L):
    # 방향 전환 전 이동 설정
    dist, dir = moves[i]
    if i > 0:
        dist -= moves[i-1][0]
    
    # 이동
    for j in range(dist):
        count += 1
        y += dy[d%4]
        x += dx[d%4]

        # 이동 위치에 본인, 벽 존재 시 종료
        if y<0 or x<0 or y>N-1 or x>N-1 or (y,x) in snake:
            isFinished = True
            break

        # 전진
        snake.append((y,x))

        # 이동 중 사과 존재 시 pop 하지않기
        if (y,x) not in apple:
            snake.popleft()
        else:
            apple.remove((y,x))

    # 이동 후 방향 전환
    if dir == "D":
        d += 1
    else:
        d -= 1
    
    if isFinished:
        print(count)
        break

# 방향전환 다해도 안부딫히는 경우
else:
    while True:
        count += 1
        y += dy[d%4]
        x += dx[d%4]

        # 이동 위치에 본인, 벽 존재 시 종료
        if y<0 or x<0 or y>N-1 or x>N-1 or (y,x) in snake:
            print(count)
            break

        # 전진
        snake.append((y,x))

        # 이동 중 사과 존재 시 pop 하지않기
        if (y,x) not in apple:
            snake.popleft()
        else:
            apple.remove((y,x))
