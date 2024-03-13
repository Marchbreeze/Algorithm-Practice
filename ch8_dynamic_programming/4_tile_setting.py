
# 정수 입력받기
n = int(input())

# DP Table 초기화하기
dpTable = [0] * 100

# 점화식을 위한 1, 2번째 값 설정
dpTable[1] = 1
dpTable[2] = 3

# 바텀업 DP 진행
for i in range(3, n+1) :
    dpTable[i] = dpTable[i-1] + dpTable[i-2] * 2

print(dpTable[n])