'''
<1300. K번째 수>
골드1
https://www.acmicpc.net/problem/1300
'''

# 문제: 크기가 N×N인 배열 A / 배열에 들어있는 수 A[i][j] = i×j / 일차원 배열에 넣은 NxN 크기의 B를 오름차순 정렬했을 때, B[k] 구하기
# 아이디어: B[k]를 파라메트릭 서치로 찾기
# - 2차원 배열일 때, mid보다 같거나 작은 값의 개수는 몫 (6보다 작은 1row : 1,2,3,4,5,6 (6//1개))
# - 단 열의 숫자(N*N배열이므로)를 초과할 수 없음
# - 총 개수 구하고, k보다 많으면 더 작은 mid, 적으면 더 큰 mid값으로 진행

n = int(input())
k = int(input())
start, end = 1, n**2
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n+1):
        count += min(n, mid//i)
    if (count >= k):
        answer = mid
        end = mid -1
    else:
        start = mid + 1

print(answer)
