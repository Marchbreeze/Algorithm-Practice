'''
<15650. N과 M (2)>
실버3
https://www.acmicpc.net/problem/15650
'''

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순

'''
조합 (Permutation) 구하기
'''

def comb(n,k):
    stack = [(1,[])]
    result = []

    while stack:
        index, saved = stack.pop()
        if len(saved) == k:
            result.append(saved)
            continue
        for i in range(n, index-1, -1):
            if i not in saved:
                stack.append((i+1, saved + [i]))
    return result

n, k = map(int, input().split())
result = comb(n, k)

for i in range(len(result)):
    print(' '.join(map(str, result[i])))