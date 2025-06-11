
# 정수 입력받기
x = int(input())

# DP Table 초기화하기
dpTable = [0] * 30001

# 바텀업 DP 진행
for i in range(2, x+1) :
    # 1을 빼기
    dpTable[i] = dpTable[i-1] + 1
    # 2로 나누기
    if (i % 2 == 0) :
        dpTable[i] = min(dpTable[i], dpTable[i//2] + 1)
    # 3으로 나누기
    if (i % 3 == 0) :
        dpTable[i] = min(dpTable[i], dpTable[i//3] + 1)
    # 5로 나누기
    if (i % 5 == 0) :
        dpTable[i] = min(dpTable[i], dpTable[i//5] + 1)

print(dpTable[x])