'''
<1205. 등수 구하기>
실버4
https://www.acmicpc.net/problem/1205
'''

# 랭킹 리스트가 100, 90, 90, 80일 때 각각의 등수는 1, 2, 2, 4등이 된다

# 리스트 요소수 N, 새점수 X, 랭킹 표시 수 P
n, x, p = map(int, input().split())

# 랭킹 점수 입력
if (n != 0):
    rank = list(map(int, input().split()))

# 랭킹 빈자리 유무 확인
isAvailable = False
if (n < p):
    isAvailable = True

# 랭킹 진입 가능 유무 확인
if (isAvailable is False and rank[n-1] >= x):
    print(-1)
else:
    myIndex = n
    for i in range(n-1,-1,-1):
        if (rank[i] > x):
            break
        else:
            myIndex -= 1
    print(myIndex+1)