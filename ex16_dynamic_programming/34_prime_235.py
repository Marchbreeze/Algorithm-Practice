'''
< 34. 못생긴 수 >
못생긴 수란, 2,3,5를 소인수로 가지는 수를 의미한다.
작은 수부터 나열할 때, n번째 못생긴 수를 찾는 프로그램을 구하시오.
(1 <= N <= 1,000)
'''

# 타겟 수 입력
n = int(input())

# 1차원 dpTable 설정
table = [0] * n

# 2,3,5배를 위한 인덱스 & 초기화된 값
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

# 1부터 n까지 숫자 찾기 (3값중 최소 찾으면 추가하고 곱셈 진행)
for j in range(1, n):
    # 3가지 경우 중 최솟값 추가
    table[j] = min(next2, next3, next5)
    # 추가된 이후 인덱스로 결과 증가
    if (table[j] == next2):
        i2 += 1
        next2 = table[i2] * 2
    if (table[j] == next3):
        i3 += 1
        next3 = table[i3] * 3
    if (table[j] == next5):
        i5 += 1
        next5 = table[i5] * 5

print(table[n-1])