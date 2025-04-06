'''
<1931. 회의실 배정>
골드5
https://www.acmicpc.net/problem/1931
'''
import sys
input = sys.stdin.readline

N = int(input())  # 회의의 수
meetings = []  # 회의 시간 리스트
result = 0  # 정답

for i in range(N):
    meetings.append(list(map(int, input().split())))

# 회의를 시작시간을 기준으로 오름차순 정렬
meetings.sort()

# 다른 회의들과 비교할 후보 회의
temp = meetings[0]

for i in range(1, N):
    # 후보 회의가 종료된 이후에 다음 회의시간이 주어진다면? 회의실을 배정하고 다음 회의를 후보 회의로 바꿈
    if temp[1] <= meetings[i][0]:
        result += 1
        temp = meetings[i]
    # 후보 회의의 종료시간이 다음 회의의 종료시간 보다 길다면? 다음 회의를 후보 회의로 바꿈
    elif temp[1] > meetings[i][1]:
        temp = meetings[i]

# 마지막 회의를 추가
result += 1

print(result)
