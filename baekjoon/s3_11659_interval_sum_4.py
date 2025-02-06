'''
<11659. 구간 합 구하기 4>
실버3
https://www.acmicpc.net/problem/11659
'''

n, m = map(int, input().split())
array_n = list(map(int, input().split()))

array = [0]
count = 0
for k in array_n:
    count += k
    array.append(count)

for _ in range(m):
    i, j = map(int, input().split())
    print(array[j]-array[i-1])