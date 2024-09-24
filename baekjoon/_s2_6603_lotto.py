'''
<6603. 로또>
실버2
https://www.acmicpc.net/problem/6603
'''

# {1, 2, ..., 49}에서 수 6개를 고름
# 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택
# ex. k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지

import itertools

# 케이스별 입력
while True:
    array = list(map(int, input().split()))
    k = array[0]
    if (k == 0):
        break
    s = array[1:]
    # 조합 라이브러리 활용
    for i in itertools.combinations(s, 6):
        print(*i)
    print("")
