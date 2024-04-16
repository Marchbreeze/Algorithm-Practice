'''
<2979. 트럭 주차>
브론즈2
https://www.acmicpc.net/problem/2979
'''

from collections import Counter

# 주차 요금 입력
fee = list(map(int, input().split()))

# 주차 시간 입력
park = [0] * 100
for i in range(3):
    x, y = map(int, input().split())
    for j in range(x-1, y-1):
        park[j] += 1

# 숫자세기
count = Counter(park)

# 결과 출력
result = 0
for i in range(3):
    result += (count[i+1] * fee[i] * (i+1))
print(result)