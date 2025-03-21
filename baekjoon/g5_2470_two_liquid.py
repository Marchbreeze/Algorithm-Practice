'''
<2470. 두 용액>
골드5
https://www.acmicpc.net/problem/2470
'''

# 리스트의 두 용액의 합으로 0에 가장 가까운 용액 제조

n = int(input())
array = list(map(int, input().split()))
array.sort()

start, end = 0, n-1
result = (array[start], array[end])
sum = array[0] + array[n-1]

while True:
    if start == end:
        break
    new_sum = array[start] + array[end]
    if abs(new_sum) < abs(sum):
        result = (array[start], array[end])
        sum = new_sum
    if new_sum > 0:
        end -= 1
    else:
        start += 1

print(result[0], result[1])