'''
<20125. 쿠키의 신체 측정>
실버4
https://www.acmicpc.net/problem/20125
'''

# 칸 크기 입력
n = int(input())

# 칸 종류 입력 & 열 개수 확인
array = []
counts = []
for i in range(n):
    letters = input()
    row = []
    count = 0
    for letter in letters:
        row.append(letter)
        if (letter == "*"):
            count += 1
    array.append(row)
    counts.append(count)

# 가로로 연속된 칸을 찾아서 팔 확인
head_row = -1
arm_row = -1
for i in range(n):
    if (counts[i] == 1):
        head_row = i
        arm_row = i + 1
        break

# 머리 좌표 확인
head_col = -1
for j in range(n):
    if (array[head_row][j] == "*"):
        head_col = j
        break

# 팔길이 확인
arm_left = 0
arm_right = 0
for j in range(head_col):
    if (array[arm_row][j] == "*"):
        arm_left += 1
for j in range(head_col+1,n):
    if (array[arm_row][j] == "*"):
        arm_right += 1
    else:
        break

# 허리길이 확인
waist = 0
for i in range(head_row+2,n):
    if (array[i][head_col] == "*"):
        waist += 1
    else:
        break

# 왼다리 확인
leg_left = 0
for i in range(head_row+2+waist,n):
    if (array[i][head_col-1] == "*"):
        leg_left += 1
    else:
        break

# 오른다리 확인
leg_right = 0
for i in range(head_row+2+waist,n):
    if (array[i][head_col+1] == "*"):
        leg_right += 1
    else:
        break

# 결과 출력
print(head_row+2,head_col+1)
print(arm_left,' ',arm_right,' ',waist,' ',leg_left,' ',leg_right)