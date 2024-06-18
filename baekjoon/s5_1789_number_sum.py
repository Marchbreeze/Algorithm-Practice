'''
<1789. 수들의 합>
실버5
https://www.acmicpc.net/problem/1789
'''

n = int(input())

sum = 0
count = 0
for i in range(1,n+5):
    sum += i
    count += 1
    if (n < sum):
        count -= 1
        break
print(count)