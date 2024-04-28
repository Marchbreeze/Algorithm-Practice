'''
<1459. 걷기>
실버4
https://www.acmicpc.net/problem/1459
'''

# 집위치x, y, 블록 시간 w, 대각선 시간 s
x, y, w, s = map(int, input().split())

# 블록, 대각선 비교
cross = False
if (s < w * 2):
    cross = True

# 가로세로 비교
short = min(x, y)
diff = abs(x - y)

# 2직선거리 비교
straight = True
if (s < w):
    straight = False

# 실행
result = 0

if (cross):
    result += s * short
else :
    result += 2 * w * short

if (straight):
    result += w * diff
else :
    if (diff % 2 == 0):
        result += s * diff
    else:
        result += s * (diff - 1)
        result += w

print(result)