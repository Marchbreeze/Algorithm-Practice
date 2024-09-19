'''
<2579. 계단 오르기>
실버3
https://www.acmicpc.net/problem/2579
'''

# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.

# 아이디어
# 최대한 많은 계단 밟아야 함
# 뒤에서부터 확인 OXOO (d[n-3]활용) OXO (d[n-2]활용)

# 계단 개수 입력 (300이하)
n = int(input())

# 계단 점수 리스트 입력
point = []
for _ in range(n):
    point.append(int(input()))

# dp 테이블 설정
d = [0] * 300

# 2번 계단까지는 수동으로 기입
d[0] = point[0]
if n > 1:
    d[1] = point[0] + point[1]
if n > 2:
    d[2] = max(point[0], point[1]) + point[2]

# 바텀업 진행
if n >= 3:
    for i in range(3, n):
        d[i] = max(d[i-3]+point[i-1]+point[i], d[i-2]+point[i])

print(d[n-1])