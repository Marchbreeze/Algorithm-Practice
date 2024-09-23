'''
<1652. 누울 자리를 찾아라>
실버5
https://www.acmicpc.net/problem/1652
'''

# NxN의 정사각형 모양의 방
# 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있음
# 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 됨

# 방 크기 받기
n = int(input())

# 벽 유무 2차원 리스트 받기
room = []
for i in range(n):
    room.append(list(input()))

# 가로 카운트
row = 0
for y in range(n):
    is_row_checked = False
    for x in range(n-1):
        if (room[y][x] == "X"):
            is_row_checked = False
        if (room[y][x] == "." and room[y][x+1] == "." and is_row_checked is False) :
            row += 1
            is_row_checked = True

# 세로 카운트
column = 0
for x in range(n):
    is_column_checked = False
    for y in range(n-1):
        if (room[y][x] == "X"):
            is_column_checked = False
        if (room[y][x] == "." and room[y+1][x] == "." and is_column_checked is False):
            column += 1
            is_column_checked = True

print(row, column)