'''
<13458. 시험 감독>
브론즈2
https://www.acmicpc.net/problem/13458
'''

# 1명의 총감독관, 여러명의 부감독관으로 필요한 감독관 수의 최솟값을 구하는 프로그램

# n개의 시험장 (1 ~ 1,000,000)
n = int(input())

# 각 A명의 응시자 (1 ~ 1,000,000)
a = list(map(int, input().split()))

# 감시 가능 응시자 수 총감독관 B, 부감독관 C (1 ~ 1,000,000)
b,c  = map(int, input().split())

count = 0
for i in range(n):
    count += 1
    a[i] -= b
    if (a[i] < 0):
        continue
    count += a[i] // c
    if (a[i] % c != 0):
        count += 1
print(count)