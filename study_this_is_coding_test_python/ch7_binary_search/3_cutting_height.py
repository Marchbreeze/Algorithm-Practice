
# 떡 개수와 필요 길이, 개별 높이 입력
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end) :
    total = 0
    mid = (start + end) // 2
    for x in array:
        if (x > mid) :
            total += x - mid
    # 부족한경우 더 많이 자르기 (왼쪽 부분탐색)
    if (total < m) :
        end = mid - 1
    # 충분한경우 더 조금 자르기 (오른쪽 부분탐색)
    else :
        result = mid
        start = mid + 1

print(result)