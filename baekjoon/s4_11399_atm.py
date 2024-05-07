'''
<11399. ATM>
실버4
https://www.acmicpc.net/problem/11399
'''

n = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0
for i in range(n):
    result += time[i]*(n-i)
print(result)