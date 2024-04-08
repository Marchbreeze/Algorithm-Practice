'''
<17266. 어두운 굴다리>
실버4
https://www.acmicpc.net/problem/17266
'''

# 가로등은 높이만큼 주위를 비출 수 있음
# 가로등의 높이가 높을수록 가격이 비싸지기 때문에 최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 함
# 가로등은 모두 높이가 같아야 함

import math

# 굴다리 길이 n, 가로등을 설치할 개수 M, 각 가로등의 위치 x
n = int(input())
m = int(input())
loc = list(map(int, input().split()))

# 위치의 최대 간격 찾기
max_interval = 0
for i in range(m-1):
    temp = loc[i+1] - loc[i]
    max_interval = max(temp, max_interval)

# 시작, 끝 간격 비교하기
max_interval = max(max_interval, loc[0]*2)
max_interval = max(max_interval, (n-loc[m-1])*2)

print(math.ceil(max_interval/2))