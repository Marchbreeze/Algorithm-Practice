'''
<17219. 비밀번호 찾기>
실버4
https://www.acmicpc.net/problem/17219
'''

n, m = map(int, input().split())

d = dict()
for _ in range(n):
    site, pw = input().split()
    d[site] = pw

for _ in range(m):
    site = input()
    print(d[site])