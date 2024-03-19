'''
<1. 모험가 길드>
N명의 모험가는 최대 N만큼의 공포도를 가지고 있다.
공포도가 X인 모험가는 반드시 X명 이상으로 모험가 그룹을 구성해야 여행을 떠날 수 있다.
최대 몇개의 모험가 그룹을 만들 수 있는지 구하시오.
(1 <= ㅜ <= 100,000)
'''

# 모험가 명수 입력받기
n = int(input())

# 각 모험가의 공포도 입력받고 정렬하기
fearList = list(map(int, input().split()))
fearList.sort(reverse=True)

# 결과값 설정하기
count = 0

# 가장 큰 수만큼 숫자 제거, 반복
while fearList:
    big = fearList[0]
    fearList.pop(0)
    count += 1
    for _ in range(big-1):
        if (fearList.count == 0):
            break
        fearList.pop(0)

print(count)