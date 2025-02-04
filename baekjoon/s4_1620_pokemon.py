'''
<1620. 나는야 포켓몬 마스터>
실버4
https://www.acmicpc.net/problem/1620
'''

n, m = map(int, input().split())
by_id = {}
by_name = {}
for i in range(1, n + 1):
    pokemon = input()
    by_id[i] = pokemon
    by_name[pokemon] = i

for _ in range(m):
    x = input()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])