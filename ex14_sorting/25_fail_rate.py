'''
< 25. 실패율 >
실패율 = 스테이지에 도달했으나 아직 클리어 못한 플레이어 수 / 도달한 플레이어 수
전체 스테이지의 개수를 N, 사용자가 멈춰있는 스테이지 배열 stages가 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호를 구하시오.
(1 <= N <= 500, 1 <= 스테이지길이 <= 200,000)
'''

# 스테이지 수 입력
n = int(input())

# 스테이지 배열 
stages = list(map(int, input().split()))

# 모든 스테이지 확인하기
new_stage = []
for i in range(1,n+1):
    complete = 0
    remain = 0
    for j in stages:
        if (j >= i):
            complete += 1
        if (j == i):
            remain += 1
    new_stage.append((i, remain/complete))

# 스테이지 정렬하기
new_stage.sort(key=lambda x: -x[1])

# 스테이지만 리스트화하기
rank = []
for i in new_stage:
    rank.append(i[0])
print(rank)