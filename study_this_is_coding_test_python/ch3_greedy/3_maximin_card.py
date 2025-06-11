
# N, M부터 입력받기
n, m = map(int, input().split())

# 한줄씩 입력받아서, 줄의 최소 수와 다른 줄의 값 비교
result = 0
for i in range(n) :
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)