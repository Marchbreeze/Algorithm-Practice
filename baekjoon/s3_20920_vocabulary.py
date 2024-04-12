'''
<20920. 영단어 암기는 괴로워>
실버3
https://www.acmicpc.net/problem/20920
'''

# 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
# 길이가 M이상인 단어만 암기

from collections import defaultdict  

# 단어 개수, 길이 기준 입력
n, m = map(int, input().split())

# 단어 받기
voca = []
for i in range(n):
    voca.append(input())

# 단어 개수 카운트
count = defaultdict()
for word in voca:
    if word not in count:
        count[word] = 0
    count[word] += 1

# 카운트 순으로 정렬된 리스트
array = list(count.items())
array.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

# 정답 출력
for word in array:
    if (len(word[0]) >= m):
        print(word[0])