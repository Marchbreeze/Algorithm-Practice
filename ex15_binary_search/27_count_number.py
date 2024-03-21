'''
< 27. 정렬된 배열에서 특정 수 개수 구하기 >
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이 수열에서 x가 등장하는 횟수를 계산하시오.
단, 시간 복잡도 O(logN)으로 설계하시오.
(1 <= N <= 1,000,000)
'''
from collections import Counter

# 원소 개수, 타겟 원소 입력
n, x = map(int, input().split())

# 리스트 입력
counter = Counter(map(int, input().split()))

# 카운터 결과 출력
print(counter[x])