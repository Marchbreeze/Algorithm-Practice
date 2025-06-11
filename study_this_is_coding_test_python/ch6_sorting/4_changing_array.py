
# N, K 입력받기
n, k = map(int, input().split())

# A, B 배열 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 오름차순, 내림차순 진행
a.sort()
b.sort(reverse=True)

# 최대 K번 비교 진행
for i in range(k) :
    if (a[i] < b[i]) :
        a[i], b[i] = b[i], a[i]
    else :
        break

print(sum(a))