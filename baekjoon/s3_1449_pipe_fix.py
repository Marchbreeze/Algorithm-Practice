'''
<1449. 수리공 항승>
실버3
https://www.acmicpc.net/problem/1449
'''

n, ll = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = n
temp = 0
for i in range(n-1):
    temp += array[i+1] - array[i]
    if (temp < ll):
        result -= 1
    else:
        temp = 0

print(result)