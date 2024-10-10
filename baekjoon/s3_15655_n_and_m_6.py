'''
<15655. N과 M (6)>
실버3
https://www.acmicpc.net/problem/15655
'''

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순

# n, m
n, m = map(int, input().split())

# N개의 자연수
num = list(map(int, input().split()))
num.sort(reverse=True)

# 순열 구하기
stack = [(0, [])]
result = []

while stack:
    index, saved = stack.pop()
    if len(saved) == m:
        result.append(saved)
        continue
    for i in num:
        if i not in saved and i > index :
            stack.append((i, saved + [i]))

for i in range(len(result)):
    print(' '.join(map(str, result[i])))