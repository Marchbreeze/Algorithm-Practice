'''
<2110. 공유기 설치>
골드4
https://www.acmicpc.net/problem/2110
'''

# 문제: 수직선 위 집 N개 중 C개에 공유기 설치 -> 가장 인접한 두 공유기 사이의 거리 최대로
# 아이디어: 사이거리 N-1개 리스트에서, 만들 수 있는 최대 거리 파라메트릭 서치

# 집 위치
n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
start = 1
end = house[-1] - house[0]

# 반복문을 활용한 파라메트릭 서치
result = 0
while start <= end:
    mid = (start + end) // 2
    # mid(거리)로 가능한 최소 공유기 개수
    current = house[0]
    count = 1
    for i in range(1, n):
        if (house[i] >= current + mid):
            count += 1
            current = house[i]
    if (count >= c):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
