
# 정수 입력받기
n,m = map(int, input().split())

# 화폐 단위 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# DP Table 설정
dpTable = [10001] * (m+1)
dpTable[0] = 0

# 바텀업 진행
for i in range(n):
    for j in range(array[i], m+1):
        dpTable[j] = min(dpTable[j], dpTable[j-array[i]] + 1)

# 결과
if (dpTable[m] == 10001):
    print(-1)
else:
    print(dpTable[m])