'''
< 11. 뱀 게임 >
뱀이 기어다니는 게임이 있다.
사과를 먹으면 뱀 길이가 늘어나고, 벽 또는 자기 자신과 부딪히면 게임이 끝난다.
게임은 NxN 보드에서 진행되고, 뱀은 길이 1로 가장 위 좌측에서 시작한다.
(2 <= N <= 100)
뱀은 매 초마다 다음과 같은 규칙으로 이동한다.
- 먼저 뱀은 몸길이를 늘려 어리를 다음 칸에 위치시킴
- 이동한 칸에 사과가 있으면, 사과를 먹고 꼬리는 움직이지 않음
- 사과가 없으면, 몸길이를 줄여 꼬리가 위치한 칸을 비워줌
K개 사과의 위치와 뱀의 이동 경로가 주어질 때, 이 게임이 몇 초만에 끝날지 구하시오.
(0 <= K <= 100, 1 <= 방향 변환 횟수 L <= 100)
'''

# 보드 크기 입력
n = int(input())

# 사과 개수 & 위치 입력
k = int(input())
apple = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    apple[x][y] = 1

# 경로 개수 & 위치 입력
ll = int(input())
route = []
for _ in range(ll):
    x, c = input().split()
    route.append((int(x),c))

# 맵 초기값 설정
length = 1
map = [[0] * n for _ in range(n)]
x = 0
y = n-1
map[x][y] = 1

# 방향 설정
rot = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 맵 이동
count = 1
flag = False
for move in route:
    for _ in range(move[0] - count - 1):
        print("(x,y):",x,y)
        nx = x + dx[rot]
        ny = y + dy[rot]
        if (nx >= n or nx < 0 or ny >= n or ny < 0):
            flag = True
            count += 1
            break

        if (apple[nx][ny] != 1):
            map[x][y] == 0

        if (map[nx][ny] != 1):
            count += 1
            x, y = nx, ny
            map[x][y] = 1 
        else:
            flag = True
            count += 1
            break

    if (flag):
        break

    if (move[1] == "L"):
        rot += 1
        if (rot == 4):
            rot = 0
    elif (move[1] == "D"):
        rot -= 1
        if (rot == -1):
            rot = 3

print(count)