'''
<1343. 폴리오미노>
실버5
https://www.acmicpc.net/problem/1343
'''

# 보드판 입력
board = input().strip()

# 하나씩 보며 연속 X 세기
temp = 0
count = []
for letter in board:
    if (letter == "X"):
        temp += 1
    else:
        if (temp != 0):
            count.append(temp)  
            temp = 0
        count.append(0)
if (temp != 0):
    count.append(temp)

# 연속 숫자 보며 값 추가하기
result = []
for i in count:
    if (i == 0):
        result.append(".")
    elif (i % 2 == 1):
        result.clear()
        break
    else:
        while True:
            if (i >= 4):
                result.append("AAAA")
                i -= 4
                if (i == 0):
                    break
            else:
                result.append("BB")
                i -= 2
                if (i == 0):
                    break

# 출력
if (len(result) == 0):
    print(-1)
else:
    print(''.join(result))