
# N,M,K 공백으로 구분해서 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분해서 입력받기
data = list(map(int, input().split()))

# 입력값 중 1, 2번째로 큰 수만 골라내기
data.sort()
first = data[n-1]
second = data[n-2]

# K개씩 first 더하고, second 한번 더하고, M번 반복
result = 0
while True :
    for i in range(k) :
        result += first
        m -= 1
        if (m == 0) : 
            break
    result += second
    m -= 1
    if (m == 0) : 
        break
print(result)
