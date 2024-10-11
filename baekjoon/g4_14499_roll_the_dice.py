'''
<14999. 주사위 굴리기>
골드4
https://www.acmicpc.net/problem/14999
'''

# 크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽
#  지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수
#   2
# 4 1 3
#   5
#   6
# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y)
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0
# 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력

# 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)
n, m, x, y, k = map(int, input().split())

# N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어짐
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
orders = list(map(int, input().split()))

# 방향으로 굴렸을 때 주사위 위치 변경 (0이 위, 5이 하단)
dice = [0,0,0,0,0,0]
def roll_dice(direction):
    a, b, c, d, e, f = dice
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

# 주사위 굴리고 출력
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for ord in orders:
    nx = x + dx[ord-1]
    ny = y + dy[ord-1]
    if nx<0 or ny<0 or nx>n-1 or ny>m-1:
        continue
    y,x = ny,nx
    roll_dice(ord)
    print(dice[0])
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0
