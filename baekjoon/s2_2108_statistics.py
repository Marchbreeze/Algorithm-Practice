'''
<2108. 통계학>
실버2
https://www.acmicpc.net/problem/2108
'''

from collections import Counter

n = int(input())
array = [int(input()) for _ in range(n)]
array.sort()

# 산술평균
print(round(sum(array)/n))

# 중앙값
print(array[n//2])

# 최빈값
most_two = Counter(array).most_common(2)
if len(most_two) == 1 or most_two[0][1] != most_two[1][1]:
    print(most_two[0][0])
else:
    print(most_two[1][0])

# 범위
print(array[-1] - array[0])