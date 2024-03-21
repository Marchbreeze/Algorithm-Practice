'''
< 28. 고정점 찾기 >
고정점 : 값과 인덱스 값이 동일한 원소
N개의 서로 다른 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
고정점을 모두 출력하시오.
'''
from bisect import bisect_right, bisect_left

# 원소 개수 입력
n = int(input())

# 원소 리스트 입력
array = list(map(int, input().split()))

# 이진 탐색
result = []
for i in range(n):
    left = bisect_left(array, i)
    right = bisect_right(array, i)
    if (left == right-1 and array[left] == left):
        result.append(left)

# 결과 출력
if (len(result) == 0):
    print(-1)
else:
    print(result[0])