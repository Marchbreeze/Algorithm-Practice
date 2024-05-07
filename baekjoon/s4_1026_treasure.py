'''
<1026. 보물>
실버4
https://www.acmicpc.net/problem/1026
'''

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# 수 입력
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
a.sort(reverse=True)

result = 0
for i in range(n):
    result += b[i]*a[i]

print(result)