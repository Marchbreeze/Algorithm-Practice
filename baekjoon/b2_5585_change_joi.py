'''
<5585. 거스름돈>
브론즈2
https://www.acmicpc.net/problem/5585
'''

# 돈 입력
n = int(input())
n = 1000 - n

# 거스름돈 도출
count = 0
if (n >= 500):
    count += n // 500
    n %= 500
if (n >= 100):
    count += n // 100
    n %= 100
if (n >= 50):
    count += n // 50
    n %= 50
if (n >= 10):
    count += n // 10
    n %= 10
if (n >= 5):
    count += n // 5
    n %= 5
count += n

print(count)