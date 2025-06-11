
# 맵 크기 입력받기
n, m = map(int, input().split())

# 캐릭터 위치, 방향 입력받기
x, y, direction = map(int, input().split())

# 전체 맵 정보 입력받기
gameMap = []
for i in range(n) :
    gameMap.append(list(map(int, input().split())))

# 동서남북 방향 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문 위치 저장용 맵 생성
visit = [[0] * m for _ in range(n)]
visit[x][y] = 1

# 왼쪽으로 회전 함수 정의
def turn_left() :
    global direction
    if (direction == 0) :
        direction = 3
    else :
        direction -= 1

# 시뮬레이션
count = 1
turn_count = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if (visit[nx][ny] == 0 and gameMap[nx][ny] == 0) :
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else :
        turn_count += 1
        if (turn_count == 4) :
            nx = x - dx[direction]
            ny = y - dy[direction]      
            if (gameMap[nx][ny] == 0) :
                x = nx
                y = ny
                turn_count = 0
            else :
                break

print(count)
