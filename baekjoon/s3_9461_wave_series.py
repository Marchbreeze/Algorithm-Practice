'''
<9461. 파도반 수열>
실버3
https://www.acmicpc.net/problem/9461
'''

t = int(input())

d = [0,1,1,1,2,2]
for i in range(6,101):
    d.append(d[i-1]+d[i-5])

for _ in range(t):
    j = int(input())
    print(d[j])
