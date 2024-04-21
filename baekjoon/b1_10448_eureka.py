'''
<10448. 유레카이론>
브론즈1
https://www.acmicpc.net/problem/10448
'''

# 테스트 개수
k = int(input())

# 삼각수 카운트
tri = [1]
for i in range(2,45):
    tri.append(tri[-1]+i)

# 하나씩 다 찾아보기
def find(n):
    for i in range(len(tri)):
        for j in range(i,len(tri)):
            for k in range(j,len(tri)):
                if tri[i]+tri[j]+tri[k] == n:
                    return 1
    return 0
for _ in range(k):
    n = int(input())
    print(find(n))
    