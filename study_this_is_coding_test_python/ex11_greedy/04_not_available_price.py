'''
<4.만들 수 없는 금액>
다양한 단위의 N개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값을 구하시오.
(1 <= N <=1,000, 1 <= 화폐단위 <= 1,000,000)

정답 아이디어 :
- 단위를 기준으로 오른차순 정렬 후, 1부터 특정 금액 만들 수 있는지 확인
- 1 ~ target-1 까지 모든 금액을 만들 수 있다면, target도 이 금액들로 만들 수 있는지 확인
- 만들 수 있다면, 값은 업데이트해가며 반복
'''

# N, 화폐단위 입력받기
n = int(input())
units = list(map(int, input().split()))
units.sort()

# 타겟 설정
target = 1

# 만들 수 없는 금액을 찾았을 때 반복 종료
for unit in units:
    if (target < unit):
        break
    target += unit

print(target)