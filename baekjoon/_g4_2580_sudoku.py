'''
<2580. 스도쿠>
골드4
https://www.acmicpc.net/problem/2580
'''
# 각 3가지 조건을 함수화한 후, DFS를 활용한 재귀로 각각의 경우 체크

sudoku = []
zeros = []
for y in range(9):
    r = list(map(int, input().split()))
    for x in range(9):
        if r[x] == 0:
            zeros.append((y, x))
    sudoku.append(r)
total = len(zeros)

def row(a, n): # 가로
    for i in range(9):
        if n == sudoku[a][i]: 
            return False
    return True

def column(a, n): # 세로
    for i in range(9):
        if n == sudoku[i][a]:
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]:
                return False
    return True

def dfs(count):
    if count == total:
        for i in sudoku:
            print(*i) 
        exit() # 강제 종료
    for i in range(1,10):
        y = zeros[count][0]
        x = zeros[count][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            dfs(count+1)
            sudoku[y][x] = 0

dfs(0)