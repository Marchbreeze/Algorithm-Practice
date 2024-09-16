'''
<2578. 빙고>
실버4
https://www.acmicpc.net/problem/2578
'''

# 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 작성
# 선이 세 개 이상 그어지는 순간 "빙고"
# 첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩
# 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩

# 1. 적은 25개 숫자를 이차원 리스트로 담음
my_list = [list(map(int, input().split())) for _ in range(5)]

# 2. 정답 순서를 리스트로 담음
speak_list = []
for _ in range(5):
    speak_list += list(map(int, input().split()))

# 3. 호명된 번호를 0으로 바꾸고, 가로세로 확인 & 대각선은 한번만
count = 0
right_top = False
left_top = False

for i in range(25):
    for x in range(5):
        for y in range(5):
            if (speak_list[i] == my_list[x][y]):
                my_list[x][y] = 0
                if (my_list[x] == [0,0,0,0,0]):
                    count += 1
                if all(my_list[j][y] == 0 for j in range(5)):
                    count += 1
                if all(my_list[i][i] == 0 for i in range(5)):
                    if (left_top is False):
                        count += 1
                        left_top = True
                if all(my_list[i][4 - i] == 0 for i in range(5)):
                    if (right_top is False):
                        count += 1
                        right_top = True
                if (count >= 3):
                    print(i+1)
                    break
        if (count >= 3):
            break
    if (count >= 3):
        break