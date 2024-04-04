'''
<7568. 덩치>
실버5
https://www.acmicpc.net/problem/7568
'''

# 정렬 규칙 : 몸무게와 키 둘다 커야 덩치가 큼 (둘중 하나면 동일)

# 사람수 입력
n = int(input())

# 각 덩치 입력
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 각 순위 담는 배열 설정
rank = [1] * n

# 모두 비교
for i in range(n):
    for j in range(i+1,n):
        if (array[i][0] > array[j][0] and array[i][1] > array[j][1]):
            rank[j] += 1
        elif (array[i][0] < array[j][0] and array[i][1] < array[j][1]):
            rank[i] += 1

# 결과 출력
for i in range(n):
    print(rank[i], end=' ')