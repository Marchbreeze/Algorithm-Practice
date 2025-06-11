'''
< 33. 병사 배치하기 >
N명의 병사가 무작위로 나열되어 있다.
각 병사는 특정 값의 전투력을 보유하고 있다.
병사를 배치할 때는 전투력이 높은 병사가 앞에 오도록 내림차순으로 배치를 한다.
배치 과정에서는 조건을 만족하지 않는 병사를 열외시킨다.
남아있는 병사가 최대가 되도록 하는 열외시킬 병사 수를 출력하시오.
(1 <= N <= 2,000)
'''

# 병사 수 입력
n = int(input())

# 전투력 리스트 입력
array = list(map(int, input().split()))

# 앞에서부터 최대 길이 세기
table = [0] * n
table[0] = 1
for i in range(1,n):
    for j in range(1,i+1):
        if (array[i] < array[i-j]):
            table[i] = max(table[i], table[i-j] + 1)

# 가장 긴 길이 찾기
result = 0
for i in table:
    result = max(result, i)

print(n - result)