'''
<10986. 나머지 합>
골드3
https://www.acmicpc.net/problem/10986
'''

n = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# 소수 리스트
primes = []
for i in range(2,n+1):
    if is_prime(i): 
        primes.append(i)

# 투 포인터
start = 0
end = 0
total = 0
cnt = 0
 
while True:
    if total == n:
        cnt += 1
        
    if total > n:
        total -= primes[start]
        start += 1
    elif end == len(primes):
        break
    else:
        total += primes[end]
        end += 1
 
print(cnt)