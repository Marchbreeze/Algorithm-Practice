'''
<1535. 안녕>
실버2
https://www.acmicpc.net/problem/1535
'''

n = int(input())
cost = list(map(int, input().split()))
joy = list(map(int, input().split()))

d = [0] * 101

for i in range(n):
    for health in range(1, 101):
        if cost[i] < health:
            d[health - cost[i]] = max(d[health - cost[i]], d[health] + joy[i])

print(max(d))