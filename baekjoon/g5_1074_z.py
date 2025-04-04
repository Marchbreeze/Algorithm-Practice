'''
<1074. Z>
골드5
https://www.acmicpc.net/problem/1074
'''

# 아이디어 : 이분탐색으로 카운트 더하기
# 예제 : N = 3 -> 가로 16, 4, 1 & 세로 32, 8, 2

n, r, c = map(int, input().split())
count = 0

# 가로(c)의 경우
start = 0
end = 2**n-1
for i in range(n):
    mid = (start + end) / 2
    if c > mid:
        count += 4**(n-1-i)
        start = mid + 0.5
    else:
        end = mid - 0.5

# 세로(r)의 경우
start = 0
end = 2**n-1
for i in range(n):
    mid = (start + end) / 2
    if r > mid:
        count += 4**(n-1-i) * 2
        start = mid + 0.5
    else:
        end = mid - 0.5
print(count)