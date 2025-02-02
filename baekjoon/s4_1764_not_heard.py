'''
<1764. 듣보잡>
실버4
https://www.acmicpc.net/problem/1764
'''

n, m = map(int, input().split())

setn = set()
for _ in range(n):
    setn.add(input())

setm = set()
for _ in range(m):
    setm.add(input())

array = sorted(list(setn & setm))

print(len(array))
for word in array:
    print(word)