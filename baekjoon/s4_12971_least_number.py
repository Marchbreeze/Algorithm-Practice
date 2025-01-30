'''
<12971. 숫자놀이>
실버4
https://www.acmicpc.net/problem/12971
'''

p1, p2, p3, x1, x2, x3 = map(int, input().split())

n = x1
while (n < 1000000000):
    if (n % p2 == x2 and n % p3 == x3):
        print(n)
        break
    n += p1
else:
    print("-1")
