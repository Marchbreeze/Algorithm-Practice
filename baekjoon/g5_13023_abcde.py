'''
<13023. ABCDE>
골드5
https://www.acmicpc.net/problem/13023
'''

import sys
sys.setrecursionlimit(100000)

n, m = map(int , input().split())
visited = [False]*(n)
adjacent = [ [] for _ in range(n) ]
arrive = False

for _ in range(m):
    a,b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

def dfs(start , depth):
    global arrive
    visited[start]=True
    if depth==5:
        arrive = True
        return
    for i in adjacent[start]:
        if visited[i] is False:
            dfs(i , depth+1)
    visited[start]=False

for i in range(n):
    dfs(i ,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)