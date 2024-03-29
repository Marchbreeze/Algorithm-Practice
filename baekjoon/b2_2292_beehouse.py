'''
<2292. 벌집>
브론즈2
https://www.acmicpc.net/problem/2292
'''

# 몇번째 껍질인지 구하면 최소 개수의 방 구할 수 있음
# 1, ~1+6, ~1+6+12, ~1+6+12+18, ...
# 1씩 빼면 0, 1~6,7~18,19~36,37~60, ...
# 6으로 나누면 0~1, 1~3, 3~6, 6~10, ...

from bisect import bisect_left, bisect_right

# 숫자 입력
num = int(input())

# 한계 숫자 1,000,000,000까지 구하기
index = 0
limit = 1
array = [1]
while limit < 1000000000:
    index += 1
    limit += 6 * index
    array.append(limit)

# 입력된 숫자 위치 구하기
array.append(num)
array.sort()
left = bisect_left(array, num)
right = bisect_right(array, num)
if (right - left == 2) :
    print(right - 1)
else :
    print(right)
    