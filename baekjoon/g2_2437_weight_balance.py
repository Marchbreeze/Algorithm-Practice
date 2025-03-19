'''
<2437. 저울>
골드2
https://www.acmicpc.net/problem/2437
'''

n = int(input())
weights = list(map(int, input().split()))
weights.sort()

if (weights[0] != 1):
    print(1)
else:
    temp = weights[0]
    for i in range(1, n):
        if (temp + 1 < weights[i]):
            break
        else:
            temp += weights[i]
    print(temp + 1)