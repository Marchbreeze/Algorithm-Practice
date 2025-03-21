'''
<2473. 세 용액>
골드3
https://www.acmicpc.net/problem/2473
'''

# 리스트의 세 용액의 합으로 0에 가장 가까운 용액 제조
# 최대 5000개 -> 하나를 골라놓고 투포인터 진행하는걸 5000번 반복해서 최대값 도출

import sys

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = [0,0,0]
sum = sys.maxsize

for fixed_index in range(1, n-1):
    start, end = 0, n-1
    while True:
        if start == end:
            break
        new_sum = array[start] + array[end] + array[fixed_index]
        if abs(new_sum) < abs(sum):
            result = [array[start], array[end], array[fixed_index]]
            sum = new_sum
        if new_sum > 0:
            end -= 1
            if (end == fixed_index):
                end -= 1
        else:
            start += 1
            if (start == fixed_index):
                start += 1

result.sort()
print(result[0], result[1], result[2])