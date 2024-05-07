'''
<11047. 코인 0>
실버4
https://www.acmicpc.net/problem/11047
'''

# 동전 종류, 동전 합
n, k = map(int, input().split())

# 오름차순 동전
array = []
for i in range(n):
    coin = int(input())
    array.append(coin)

# 하나씩 분류
count = 0
for i in range(n-1,-1,-1):
    count += k // array[i]
    k %= array[i]

print(count)