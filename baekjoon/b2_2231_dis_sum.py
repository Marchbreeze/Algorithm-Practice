'''
<2231. 분해합>
브론즈2
https://www.acmicpc.net/problem/2231
'''

# N은 최대 7자리 -> 일, 십의자리만 가능

# 숫자 입력
n = int(input())

# 숫자 자리수 확인
digit = len(str(n))

# 하나씩 진행
isMade = False
start = 0
if (n > 20) :
    start = n - digit*9
for i in range(start, n+1):
    hap = i
    for j in str(i):
        hap += int(j)
    if (hap == n):
        print(i)
        isMade = True
        break

if (isMade is not True):
    print(0)