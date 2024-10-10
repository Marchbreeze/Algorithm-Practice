'''
<15651. N과 M (3)>
실버3
https://www.acmicpc.net/problem/15651
'''

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨

'''
중복 순열 구하기
'''

def perm(n,k):
    stack = [[]]
    result = []

    while stack:
        saved = stack.pop()
        if len(saved) == k:
            result.append(saved)
            continue
        for i in range(n,0,-1):
                stack.append(saved + [i])
    return result

n, k = map(int, input().split())
permutations = perm(n, k)

for i in range(len(permutations)):
    print(' '.join(map(str, permutations[i])))