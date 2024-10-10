'''
<1759. 암호 만들기>
골드5
https://www.acmicpc.net/problem/1759
'''

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열

'''
예시 atcisw : 모자자모자자
1. 정렬 acistw
2. 백트래킹 진행 & 진행 과정에서 모음, 자음 개수 카운트
'''

# L개의 서로 다은 알파벳으로 구성, 가능한 알파벳 C가지
L, C = map(int, input().split())
arr = list(input().split())

# 알파벳 리스트 정렬
arr.sort()
result = []

# 백트래킹 진행 (리스트, 인덱스, 모음개수, 자음개수)
stack = [([],0,0,0)]
while stack:
    saved, index, mo, ja = stack.pop()
    if len(saved) == L:
        if mo>=1 and ja>=2:
            result.append(saved)
        continue
    for i in range(index, C):
        mo_i = mo
        ja_i = ja
        if arr[i] in ['a','e','i','o','u']:
            mo_i += 1
        else:
            ja_i += 1
        stack.append((saved + [arr[i]], i+1, mo_i, ja_i))

for i in range(len(result)-1,-1,-1):
    print(''.join(result[i]))