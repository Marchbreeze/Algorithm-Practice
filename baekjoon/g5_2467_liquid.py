'''
<2467. 용액>
골드5
https://www.acmicpc.net/problem/2467
'''

n = int(input())
liquid = [int(x) for x in input().split()]

value = int(1e9)
x, y = 0, 0
left = 0
right = n - 1

while left < right:
    hap = liquid[left] + liquid[right]

    if abs(hap) <= value:
        x = liquid[left]
        y = liquid[right]
        value = abs(hap)

    if hap <= 0:
        left += 1

    else:
        right -= 1

print(x, y)