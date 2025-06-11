'''
<05. 볼링공 고르기>
A, B 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
총 N개의 볼링공은 1~M 사이의 무게가 적혀있고, 1~N의 번호를 가지고 있다.
두 사람이 볼링공을 고르는 경우의 수를 구하시오
(1 <= N <= 1,000, 1 <= M <= 10)
'''

# 볼링공 개수, 공의 최대 무게 입력받기
n, m = map(int, input().split())

# 볼링공 무게 리스트 받기
weight = list(map(int, input().split()))

# 경우 하나씩 세기
count = 0

# 같은 무게 아닌 경우 모두 세기
for i in range(n):
    now = weight[i]
    for j in range(i, n):
        if (now != weight[j]):
            count += 1

# 결과 출력하기
print(count)