'''
<21921. 블로그>
실버3
https://www.acmicpc.net/problem/21921
'''
from collections import Counter
import sys
input = sys.stdin.readline

# N일 운영 중 x일동안 가장 많이 들어온 방문자 수
n, x = map(int, input().split())

# 방문자 수 입력
array = list(map(int, input().split()))

# x개씩 합 배열 생성
hap = []
value = sum(array[:x])
hap.append(value)
for i in range(x,n):
    value += array[i]
    value -= array[i-x]
    hap.append(value)

# 정렬
count = Counter(hap).most_common()
count.sort(key=lambda x: -x[0])

# 출력
if (count[0][0] == 0):
    print("SAD")
else :
    print(count[0][0])
    print(count[0][1])
