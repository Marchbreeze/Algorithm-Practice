'''
<1159. 농구 경기>
브론즈2
https://www.acmicpc.net/problem/1159
'''

from collections import defaultdict 

# 선수 수 입력
n = int(input())

# 입력받기
count = defaultdict()
for _ in range(n):
    word = input().strip()
    if word[0] not in count:
        count[word[0]] = 0
    count[word[0]] += 1

# 5 넘는 성 찾기
array = list(count.items())
result = []
for i in range(len(array)):
    if (array[i][1] >= 5):
        result.append(array[i][0])

# 결과 출력
if (len(result) == 0):
    print("PREDAJA")
else:
    result.sort(key=lambda x: x[0])
    print(''.join(result))