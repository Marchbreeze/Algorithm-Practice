
# 나이트의 위치 입력받기 - a1
start = input()
row = int(start[1])
column = int(ord(start[0])) - int(ord('a')) + 1

# 나이트 이동 방향 정의
steps = [(-2,-1), (-1,-2), (-2,1), (-1,2), (2,-1), (1,-2), (2,1), (1,2)]

# 8가지 경우에 대해서 가능 여부 확인
count = 0
for step in steps :
    new_row = row + step[0]
    new_column = column + step[1]
    if (1 <= new_row <= 8 and 1 <= new_column <= 8) :
        count += 1

print(count)
