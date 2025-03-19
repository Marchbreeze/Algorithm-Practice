'''
<1339. 단어 수학>
골드4
https://www.acmicpc.net/problem/1339
'''

from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    word = input()
    m = len(word)
    for i in range(m):
        d[word[i]] += 10**(m-i-1)

array = list(d.items())
array.sort(key=lambda x: -x[1])

result = 0
for i in range(len(array)):
    result += array[i][1] * (9-i)
print(result)