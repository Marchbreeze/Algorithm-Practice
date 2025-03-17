'''
<2841. 외계인의 기타 연주>
실버1
https://www.acmicpc.net/problem/2841
'''

from collections import deque

guitar = [deque() for _ in range(6)]
n, p = map(int, input().split())
total = 0
for _ in range(n):
    line, pret = map(int, input().split())
    while True:
        if (len(guitar[line-1]) == 0):
            guitar[line-1].append(pret)
            total += 1
            break
        highest = guitar[line-1].pop()
        if (pret > highest):
            guitar[line-1].append(highest)
            guitar[line-1].append(pret)
            total += 1
            break
        elif (pret == highest):
            guitar[line-1].append(pret)
            break
        else:
            total += 1
print(total)