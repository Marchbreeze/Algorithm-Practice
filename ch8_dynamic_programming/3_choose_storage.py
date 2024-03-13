
# 정수, 식량 리스트 입력받기
x = int(input())
array = list(map(int, input().split()))

# DP Table 초기화하기
dpTable = [0] * 100

# 점화식을 위한 0, 1번째 값 설정
dpTable[0] = array[0]
dpTable[1] = max(array[0], array[1])

# 바텀업 DP 진행
for i in range(2, x) :
    dpTable[i] = max(dpTable[i-1], dpTable[i-2] + array[i])

print(dpTable[x-1])