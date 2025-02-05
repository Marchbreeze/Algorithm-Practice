'''
<17626. Four Squares>
실버3
https://www.acmicpc.net/problem/17626
'''

n = int(input())
count = 0

d = [0] * (n + 1)

k = 1
while k**2 <= n:
    d[k**2] = 1
    k += 1

for i in range(1, n + 1):
    if d[i] != 0:
        continue
    j = 1
    while j*j <= i:
        if d[i] == 0:
            d[i] = d[j*j] + d[i - j*j]
        else:
            d[i] = min(d[i], d[j*j] + d[i - j*j])
        j += 1
print(d[n])