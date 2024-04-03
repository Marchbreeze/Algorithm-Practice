'''
<8979. 올림픽>
실버5
https://www.acmicpc.net/problem/8979
'''

# 순서 : 금 > 금동일시 은 > 금은동일시 동

# 국가 수, 등수 알고싶은 국가 입력
n, k = map(int, input().split())

# 국가 정보 입력
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 순서 나열
array.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

# 등수 찾기
rank = 0
medal = []
for i in range(n):
    if (array[i][0] == k):
        rank = i+1
        medal.append(array[i][1])
        medal.append(array[i][2])
        medal.append(array[i][3])

# 공동 등수 찾기
for i in range(rank-1):
    if (array[i][1] == medal[0] and array[i][2] == medal[1] and array[i][3] == medal[2]):
        rank -= 1

print(rank)