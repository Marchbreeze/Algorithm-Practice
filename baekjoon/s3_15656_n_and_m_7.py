'''
<15656. N과 M (7)>
실버3
https://www.acmicpc.net/problem/15656
'''

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

'''
중복 순열 구하기
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

stack = [[]]
result = []

while stack:
    saved = stack.pop()
    if len(saved) == k:
        result.append(saved)
        continue
    for i in arr:
            stack.append(saved + [i])

for i in range(len(result)):
    print(' '.join(map(str, result[i])))