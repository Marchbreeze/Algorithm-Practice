'''
<1463. 1로 만들기>
실버3
https://www.acmicpc.net/problem/1463
'''

# 연산 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 연산 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 연산 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력

# 숫자 입력
n = int(input())

# dp테이블 생성
array = [0] * 1000001
array[2] = 1
array[3] = 1

# 바텀업 진행
for i in range(4,n+1):
    array[i] = array[i-1] + 1
    if (i % 2 == 0):
       array[i] = min(array[i], array[i // 2] + 1)
    if (i % 3 == 0):
       array[i] = min(array[i], array[i // 3] + 1)

print(array[n])