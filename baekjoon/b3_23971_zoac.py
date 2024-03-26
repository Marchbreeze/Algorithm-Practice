'''
<23971. ZOAC 4>
브론즈3
https://www.acmicpc.net/problem/23971
'''

import math

# W열, H행 & 세로로 N칸, 가로로 M칸 띄우고 앉기
h, w, n, m = map(int, input().split())

# 일단 (0,0)에 앉히고, 최대한 붙여서 진행
max_h = math.ceil(h / (n+1))
max_w = math.ceil(w / (m+1))

print(max_h * max_w)