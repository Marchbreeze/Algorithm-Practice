'''
<10775. 공항>
골드2
https://www.acmicpc.net/problem/10775
'''

# 1~G번의 게이트, P개의 비행기가 순서대로 도착
# i번째 비행기를 1~gi번째 게이트 중 하나에 도킹 (한 게이트에 비행기 하나, 어느 게이트에도 도킹 못하면 폐쇄)

g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]

parent = [i for i in range(10**5+1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x] 

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

count = 0
for plane in planes:
    new = find_parent(plane)
    if (new == 0):
        break
    union_parent(new, new-1)
    count += 1

print(count)