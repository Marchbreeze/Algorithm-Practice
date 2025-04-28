'''
<1929. 소수 구하기>
실버3
https://www.acmicpc.net/problem/1929
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

m, n = map(int, input().split())
for num in range(m, n+1):
    if is_prime(num):
        print(num)