'''
< 32. 정수 삼각형 >
N층의 정삼각형 배열의 삼각형이 있다.
맨 위부터 시작해서 아래로 하나씩 내려올 때, 선택된 수의 합이 최대가 되도록 구하시오.
(1 <= N <= 500, 0 <= 수 <= 9999)
'''

# 크기 입력
n = int(input())

# 삼각형 입력 
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

# 위층부터 각 자리에 최대합 저장
for i in range(1,n):
    for j in range(i+1):
        post = 0
        if (j != 0):
            post = max(post, tri[i-1][j-1])
        if (j != i):
            post = max(post, tri[i-1][j])
        tri[i][j] += post

# 결과 출력
result = 0
for i in tri[n-1]:
    result = max(result, i)
print(result)