
# 좌표 크기 입력받기
n = int(input())

# 계획서 입력받기
x, y = 1, 1
plans = input().split()

# 이동 방향 설정하기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 공간을 넘지 않는 경우 이동하기
for plan in plans :
    for i in range(len(move_types)) :
        if (plan == move_types[i]) :
            nx = x + dx[i]
            ny = y + dy[i]
    if (1 <= nx <= n and 1 <= ny <= n) :
        x, y = nx, ny

print(x, y)
