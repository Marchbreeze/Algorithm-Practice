'''
<1038. 감소하는 수>
골드5
https://www.acmicpc.net/problem/1038
'''

import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
answer = []

# 반복문을 통해 감소하는 수를 조합
# 최소 감소하는 수는 0, 최대 감소하는 수는 9876543210 
# 즉, 최소 자릿수 개수는 1, 최대 자릿수 개수는 10
for i in range(1, 11): # 자릿수에 맞게 1부터 10까지 반복
    for j in combinations(range(10), i): 
        num = sorted(list(j), reverse=True) # 감소하는 수이므로 reverse=True 하여 정렬 수행
        answer.append(int("".join(map(str, num))))

answer.sort()  # 결과 리스트 자체 정렬
print(answer[n] if len(answer) > n else -1)  # 감소하는 수가 있을 때와 없는 경우