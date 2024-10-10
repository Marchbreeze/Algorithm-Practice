'''
<16926. 배열 돌리기 1>
골드5
https://www.acmicpc.net/problem/1759
'''

from collections import deque

'''
배열은 다음과 같이 반시계 방향으로 돌려야 한다.

A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
   ↓                                       ↑
A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
   ↓         ↓                   ↑         ↑
A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
   ↓                                       ↑
A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
'''

'''
회전수 = min(N,M) // 2
deque.rotate(n) : 원형큐처럼 회전 가능
deque.extend([]) : 여러 값 추가 가능
'''

# 배열 크기 N, M, 회전 수 R
n, m, r = map(int, input().split())
loop = min(n,m) // 2

# 초기 배열 설정
arr = []
for i in range(n):
    arr.append(list(input().split()))

# 새로 설정할 배열
new_arr = [[0] * m for _ in range(n)]

# 큐에 기존 배열 넣고 rotate 후 재배치
for i in range(loop):
    q = deque()

    # 기존 배열 채워넣기
    q.extend(arr[i][i:m-i])
    q.extend([row[m-i-1] for row in arr[i+1:n-i-1]])
    q.extend(arr[n-i-1][i:m-i][::-1])
    q.extend([row[i] for row in arr[i+1:n-i-1]][::-1])
    
    # 회전
    q.rotate(-r)
    
    # 회전된 배열 채워넣기
    for j in range(i, m-i):              
        new_arr[i][j] = q.popleft()
    for j in range(i+1, n-i-1):             
        new_arr[j][m-i-1] = q.popleft()
    for j in range(m-i-1, i-1, -1):         
        new_arr[n-i-1][j] = q.popleft()  
    for j in range(n-i-2, i, -1):    
        new_arr[j][i] = q.popleft()    

for line in new_arr:
    print(" ".join(line))