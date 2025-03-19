'''
<1654. 랜선 자르기>
실버2
https://www.acmicpc.net/problem/1654
'''

# 문제: 길이가 제각각인 K개 랜선을 정수 길이만큼 잘라버려서 -> 같은 길이의 N개 이상의 랜선 만들기 
# 아이디어: 특정 길이를 설정 후 가능 개수를 파악한 후, N개 이상이면 더 긴 길이, 이하면 더 짧은 길이를 찾으며 파라메트릭 서치

# K, N, K개의 랜선 길이
k, m = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

# 정렬 후 가능한 길이 범위 확인
lans.sort()
start = 1
end = lans[-1]
result = 0

# 반복문을 활용한 파라메트릭 서치
while start <= end:
    mid = (start + end) // 2
    pieces = 0
    for lan in lans:
        pieces += lan // mid
    if (pieces >= m):
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)
