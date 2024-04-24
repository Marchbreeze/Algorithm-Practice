'''
<9501. 꿈의 우주여행>
브론즈3
https://www.acmicpc.net/problem/9501
'''

# 테스트 케이스 T
t = int(input())

# 반복
for _ in range(t):
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        v, f, c = map(int, input().split())
        if (v*f/c >= d):
            count += 1
    print(count)
