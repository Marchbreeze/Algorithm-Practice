'''
<1244. 스위치 켜고 끄기>
실버4
https://www.acmicpc.net/problem/1244
'''

# ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다
# 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다

# 스위치 개수 입력
n = int(input())

# 스위치 상태 입력
switch = list(map(int, input().split()))

# 상태 변환
def change_switch(num):
    if (switch[num] == 1):
        switch[num] = 0
    else:
        switch[num] = 1

# 남학생 상태 변환
def change_male(num):
    for i in range(num-1,n,num):
        change_switch(i)

# 여학생 상태 변환
def change_female(num):
    change_switch(num-1)
    for i in range(1,n//2):
        if (num-1-i < 0 or num-1+i > n-1):
            break
        if (switch[num-1-i] == switch[num-1+i]):
            change_switch(num-1-i)
            change_switch(num-1+i)
        else:
            break

# 학생 수 입력
m = int(input())

# 학생 성별, 숫자 입력
for _ in range(m):
    gender, num = map(int, input().split())
    if (gender == 1):
        change_male(num)
    else:
        change_female(num)

# 출력
max_per_line = 20
output_string = ""
for i, value in enumerate(switch):
    output_string += str(value) + " "
    if (i + 1) % max_per_line == 0:
        output_string += "\n"

print(output_string)