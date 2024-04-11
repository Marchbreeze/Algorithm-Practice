'''
<13305. 주유소>
실버3
https://www.acmicpc.net/problem/13305
'''

# 일직선 도로 위 N개의 도시가 있다
# 제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동하려고 한다
# 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다. 기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다.
# 이동할 때 1km마다 1리터의 기름을 사용한다. 각 도시에는 하나의 주유소가 있으며, 주유소의 리터당 가격은 다를 수 있다.

import sys
input = sys.stdin.readline

# 도시 개수 입력
n = int(input())

# 도로의 길이 리스트 입력
length = list(map(int, input().split()))

# 주유소 리터당 가격 입력
oil = list(map(int, input().split()))

minPrice = oil[0]
total = 0

for i in range(n-1):
    if minPrice > oil[i]:
        minPrice = oil[i]

    total += (minPrice * length[i])
    
print(total)