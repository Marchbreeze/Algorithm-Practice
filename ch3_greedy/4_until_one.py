
# N,K 입력받기
n, k = map(int, input().split())
result = 0

# 남은 N이 K 이상인 경우 계속 나누기
while (n >= k) :
    if (n % k == 0) :
        n //= k
    else : 
        n -= 1
    result += 1

# 모두 나눈 후 1까지 빼기 진행하기
result += (n-1)

print(result)