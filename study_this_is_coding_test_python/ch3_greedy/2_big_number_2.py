
# N,M,K 공백으로 구분해서 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분해서 입력받기
data = list(map(int, input().split()))

# 입력값 중 1, 2번째로 큰 수만 골라내기
data.sort()
first = data[n-1]
second = data[n-2]

# 반복되는 수열 계산
chunk = m//(k+1)
remainder = m%(k+1)

# second 설정
result = chunk * second

# first 설정
result += (chunk * k +  remainder) * first

print(result)
