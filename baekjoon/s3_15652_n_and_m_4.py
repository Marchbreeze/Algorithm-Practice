'''
<15652. N과 M (4)>
실버3
https://www.acmicpc.net/problem/15652
'''

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨
# 고른 수열은 비내림차순

def comb(n,k):
    stack = [(1,[])]
    result = []

    while stack:
        index, saved = stack.pop()
        if len(saved) == k:
            result.append(saved)
            continue
        for i in range(n, index-1, -1):
                stack.append((i, saved + [i]))
    return result

n, k = map(int, input().split())
result = comb(n, k)

for i in range(len(result)):
    print(' '.join(map(str, result[i])))