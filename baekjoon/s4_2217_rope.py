'''
<2217. 로프>
실버4
https://www.acmicpc.net/problem/2217
'''

# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때
# 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
# 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량 구하기

# 로프 개수
n = int(input())

# 각 최대 중량
array = []
for i in range(n):
    weight = int(input())
    array.append(weight)

# 찾기
array.sort()
result = 0
for i in range(n):
    result = max(result, array[i] * (n-i))
print(result)
