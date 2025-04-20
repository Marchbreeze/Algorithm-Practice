'''
<1987. 알파벳>
골드4
https://www.acmicpc.net/problem/1987
'''

# 알파벳 리스트 들고다니는 것보다, 26개 T/F 불린 리스트가 메모리 측면에서 효율적!! (수정 필요)

r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

stack = []
stack.append((0,0,[array[0][0]],1))
count = 1

while stack:
    y, x, alpha, cnt = stack.pop()
    count = max(count, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (nx<0 or nx>c-1 or ny<0 or ny>r-1):
            continue
        if (array[ny][nx] in alpha):
            continue
        stack.append((ny, nx, alpha + [array[ny][nx]], cnt+1))

print(count)