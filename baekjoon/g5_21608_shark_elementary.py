'''
<21608. 상어 초등학교>
골드5
https://www.acmicpc.net/problem/21608
'''

# 교실은 N×N 크기의 격자로 나타낼 수 있다. 학교에 다니는 학생의 수는 N^2명
# 학생은 1번부터 N2번까지 번호가 매겨져 있고, (r, c)는 r행 c열을 의미
# 선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사
# 자리 배치 규칙 :
# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# N 입력
n = int(input())

# 학생 선호도 입력 (빈 0인덱스 포함) & 순서 기록
like = [[] for _ in range(n**2+1)]
order = []

for _ in range(n**2):
    i, a, b, c, d = map(int, input().split())
    like[i].extend([a,b,c,d])
    order.append(i)

# 방배치 설정
board = [[0] * n for _ in range(n)]

# 방향 설정
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def out_of_range(y, x):
    return x < 0 or x > n-1 or y < 0 or y > n-1

# 학생 순서대로 규칙 지키기
for i in order:
    max_like = 0
    seat_like = [] # (y,x,빈자리,좋아요)
    for y in range(n):
        for x in range(n):
            # 인접 좋아요 개수, 빈자리 개수 확인
            if board[y][x] == 0:
                count_like = 0 
                count_empty = 0
                for j in range(4):
                    ny = y + dy[j]
                    nx = x + dx[j]
                    if out_of_range(ny,nx):
                        continue
                    near = board[ny][nx]
                    if near == 0:
                        count_empty += 1
                    elif near in like[i]:
                        count_like += 1
                # max_like랑 비교한 후 기록
                if max_like > count_like:
                    continue
                elif max_like < count_like:
                    max_like = count_like
                    seat_like.clear()
                seat_like.append((y,x,count_empty))
    # 자리 결정
    if len(seat_like) != 1:
        seat_like.sort(key=lambda x: (-x[2], x[0], x[1]))
    if len(seat_like) != 0:
        y, x, e = seat_like[0]
        board[y][x] = i

# 인접 좋아 개수 카운트
count = [0] * (n**2+1)
for y in range(n):
    for x in range(n):
        num = board[y][x]
        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]
            if out_of_range(ny,nx):
                continue
            near = board[ny][nx]
            if near in like[num]:
                count[num] += 1

# 점수 계산
result = 0
for i in count:
    if i==0:
        continue
    else:
        result += 10**(i-1)
print(result)