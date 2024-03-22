'''
< 31. 금광 >
N x M 크기의 금광에는 특정 크기의 금이 있다.
채굴자는 첫번째 열의 어느 행에서 출발할 수 있다.
이후 m번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나로 이동한다.
채굴자가 얻을 수 있는 금의 최대 크기를 구하시오.
()
'''

# 금광 크기 입력
n, m = map(int, input().split())

# 금 개수 입력
input_array = list(map(int, input().split()))
gold = []
index = 0
for i in range(n):
    gold.append(input_array[index:index+m])
    index += m

# dpTable 설정 & 1열 값 설정
table = [[0] * m for _ in range(n)]
for i in range(n):
    table[i][0] = gold[i][0]

# 2열부터 이전 열 비교 후 최대 값 선택
for i in range(1,m):
    for j in range(n):
        result = table[j][i-1]
        if (j != 0):
            result = max(result, table[j-1][i-1])
        if (j != n-1):
            result = max(result, table[j+1][i-1])
        table[j][i] = result + gold[j][i]

# dpTable에서 가장 큰 값 탐색
max_gold = 0
for i in range(n):
    max_gold = max(max_gold, table[i][n])

print(max_gold)